import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse
import translations as tr

def render(p, t, scoring):
    st.header(t("sim_title"))
    st.markdown("""
    This tool simulates how your score changes over time.
    **Crucial:** It accounts for **Age Decay**. As you gain experience (points up), you also get older (points down).
    """)

    # --- 0. ROBUST INPUT SANITIZATION ---
    def safe_get(key):
        val = p.get(key, 0)
        if val is None: return 0
        if isinstance(val, (int, float)): return int(val)
        if isinstance(val, str):
            val = val.strip()
            if not val: return 0
            if not val.isnumeric(): return 0
        return int(float(val))

    # Clean inputs for simulation math
    age_val = safe_get('age')
    edu_val = p.get('edu', '')
    exp_val = safe_get('gen_exp')
    qc_exp_val = safe_get('qc_exp')

    # French Skills
    fr_r_val = safe_get('fr_r')
    fr_w_val = safe_get('fr_w')

    # Spouse inputs
    has_spouse = bool(p.get('spouse'))
    sp_age_val = safe_get('sp_age')
    sp_qc_exp_val = safe_get('sp_qc_exp')
    sp_fr_l_val = safe_get('sp_fr_l')
    sp_fr_s_val = safe_get('sp_fr_s')

    # --- 1. TARGET SELECTION ---
    st.subheader(t("step1"))
    draw_options = [t("manual")] + [f"{d['Date']} - {d['Stream']} ({d['Score']} pts)" for d in scoring.LATEST_DRAWS]

    c_sel, c_score = st.columns([3, 1])
    target_selection = c_sel.selectbox(t("select_draw"), draw_options, index=0)

    target_score = 600
    target_stream_name = "Manual Target"

    if target_selection == t("manual"):
        target_score = c_score.number_input("Target Score", 500, 900, 600)
    else:
        for d in scoring.LATEST_DRAWS:
            if f"{d['Date']} - {d['Stream']} ({d['Score']} pts)" == target_selection:
                target_score = d['Score']
                target_stream_name = d['Stream']
                break

        color = "#16a34a"
        c_score.markdown(f"""
        <div style="background-color:#f0fdf4; border:1px solid {color}; color:{color}; padding:10px; border-radius:6px; text-align:center;">
            <small style="color:#666; font-size:0.7em; line-height:1.1; display:block; margin-bottom:5px;">{target_stream_name}</small>
            <strong style="font-size:1.6rem;">{target_score}</strong>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # --- 2. PARAMETERS ---
    st.subheader(t("step2"))

    # FILTER: Exclude 'sp_fr_target' from the list of keys
    # We use a list comprehension to keep everything EXCEPT Spouse French
    axis_display_opts = [
        k for k in tr.AXIS_MAP_LABELS.keys()
        if k != 'sp_fr_target'
    ]

    # Map the keys to their translated labels for the dropdown
    axis_display_labels = [tr.AXIS_MAP_LABELS[k][st.session_state.lang] for k in axis_display_opts]

    col_x, col_y = st.columns(2)
    x_label_sel = col_x.selectbox(t("x_axis"), axis_display_labels, index=0)

    # Logic to ensure we don't crash if the default index (1) is out of bounds
    default_y_index = 1 if len(axis_display_labels) > 1 else 0
    y_label_sel = col_y.selectbox(t("y_axis"), axis_display_labels, index=default_y_index)

    # Reverse lookup: Find the key based on the selected label
    x_key = next(k for k, v in tr.AXIS_MAP_LABELS.items() if v[st.session_state.lang] == x_label_sel)
    y_key = next(k for k, v in tr.AXIS_MAP_LABELS.items() if v[st.session_state.lang] == y_label_sel)

    def get_range(k):
        if k == 'time_travel': return [0, 6, 12, 18, 24, 30, 36, 48, 60]
        if 'fr' in k: return [4, 5, 6, 7, 8, 9, 10, 12]
        return []

    x_vals = get_range(x_key)
    y_vals = get_range(y_key)

# --- 3. SIMULATION LOOP ---
    results = []

    # Import pandas here just in case (though it's likely at top of file)
    import pandas as pd

    for y_val in y_vals:
        for x_val in x_vals:
            sim = p.copy()

            # Define the logic function inside the loop to capture variables
            def apply_sim_logic(key, val):
                if key == 'time_travel':
                    years_passed = int(val / 12)
                    sim['age'] = age_val + years_passed
                    if has_spouse: sim['sp_age'] = sp_age_val + years_passed

                    sim['qc_exp'] = qc_exp_val + val
                    sim['prim_occ_exp'] = safe_get('prim_occ_exp') + val
                    sim['gen_exp'] = exp_val + val

                    if has_spouse: sim['sp_qc_exp'] = sp_qc_exp_val + val

                    curr_out_res = safe_get('out_res')
                    if curr_out_res > 0: sim['out_res'] = curr_out_res + val

                    curr_out_work = safe_get('out_work')
                    if curr_out_work > 0: sim['out_work'] = curr_out_work + val

                elif key == 'fr_target':
                    sim['fr_l'] = sim['fr_s'] = sim['fr_r'] = sim['fr_w'] = val
                elif key == 'sp_fr_target':
                    sim['sp_fr_l'] = sim['sp_fr_s'] = sim['sp_fr_r'] = sim['sp_fr_w'] = val

            apply_sim_logic(x_key, x_val)
            apply_sim_logic(y_key, y_val)

            # --- NEW: CALCULATE DATE ---
            # We assume x_val is "months passed".
            # If x_axis is NOT time_travel, x_val might be something else,
            # but usually "time_travel" is the only time-based axis in your app.

            months_passed = 0
            if x_key == 'time_travel': months_passed = x_val
            elif y_key == 'time_travel': months_passed = y_val

            future_date = pd.Timestamp.now() + pd.DateOffset(months=months_passed)
            date_str = future_date.strftime("%b %Y") # e.g. "Nov 2026"

            score, _ = scoring.calculate_score(sim)

            # SAVE DATA
            results.append({
                "x": x_val,
                "y": y_val,
                "score": score,
                "age": sim.get('age', age_val), # Save the simulated age
                "date": date_str                # Save the calculated date
            })

    # --- 4. VISUALIZATION ---
    # 1. CREATE DATAFRAME & TEXT
    df_sim = pd.DataFrame(results)

    df_sim["tooltip"] = df_sim.apply(
        lambda row: (
            f"<b>{y_label_sel}: {row['y']}</b><br>"
            f"<b>{x_label_sel}: {row['x']}</b><br><br>"
            f"<b>📅 Date: {row.get('date', 'N/A')}</b><br>"
            f"<b>🎂 Age: {row.get('age', 'N/A')}</b><br>"
            f"<b>🏆 Score: {row['score']}</b>"
        ),
        axis=1
    )

    # 2. PREPARE DATA
    pivot_df = df_sim.pivot(index="y", columns="x", values="score").sort_index()
    p_tooltip = df_sim.pivot(index="y", columns="x", values="tooltip").sort_index()

    # 3. COLOR LOGIC (Gradient Red -> Static Green)
    min_val = pivot_df.min().min()
    max_val = pivot_df.max().max()

    # Avoid divide-by-zero
    if max_val == min_val: max_val += 1

    # Calculate the Cutoff Ratio
    if target_score >= max_val:
        mid_ratio = 1.0
    elif target_score <= min_val:
        mid_ratio = 0.0
    else:
        mid_ratio = (target_score - min_val) / (max_val - min_val)

    # --- THE COLOR FIX ---
    # 1. Start at Dark Red
    # 2. Fade to Very Light Red right before the target
    # 3. Switch to Solid Green AT the target
    # 4. Stay Solid Green until the max score
    custom_colors = [
        [0.0, "#7f1d1d"],       # Darkest Red (Worst Score)
        [mid_ratio, "#fca5a5"], # Lightest Red (Almost there)
        [mid_ratio, "#16a34a"], # Solid Green (Target Reached)
        [1.0, "#16a34a"]        # Solid Green (Max Score - SAME COLOR)
    ]

    # 4. DRAW CHART
    fig = px.imshow(
        pivot_df,
        text_auto=False,
        aspect="auto",
        color_continuous_scale=custom_colors,
        range_color=[min_val, max_val]
    )

    # 5. UPDATE TRACES
    fig.update_traces(
        text=pivot_df.values,
        texttemplate="%{text}",
        customdata=p_tooltip.values.tolist(),
        hovertemplate="%{customdata}<extra></extra>"
    )

    # 6. LAYOUT
    fig.update_layout(
        title=dict(text=t("green_zone").format(score=target_score), x=0.5),
        xaxis=dict(title=x_label_sel, side="bottom", type='category'),
        yaxis=dict(title=y_label_sel, type='category'),
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=40, b=0)
    )

    st.plotly_chart(fig, width='stretch')

    # --- 5. EXPLANATION FORMULA ---
    st.markdown("### 📐 How is this calculated?")

    st.markdown(r"""
    The simulation recalculates your official score for **every single square** in the grid.
    It assumes you continue working in your current role:

    $$
    \text{Future Score} = \text{Current Profile} + \underbrace{\text{Tenure Gain}}_{\color{green}{\text{Points } \uparrow}} - \underbrace{\text{Age Decay}}_{\color{red}{\text{Points } \downarrow}} + \underbrace{\text{Target French}}_{\color{blue}{\text{New Skill Level}}}
    $$
    """)

    with st.expander("ℹ️ Click to see exactly what changes"):
        st.markdown(f"""
        1.  **Start:** We take your current profile (Age: **{age_val}**, Experience: **{exp_val}** months).
        2.  **Apply Time Travel:** For every month passed on the axis, we update:
            * ✅ **General & Quebec Experience:** You gain 1 month of experience.
            * ✅ **Shortage Job Tenure:** Your primary occupation tenure increases (re-calculating shortage points).
            * ✅ **Spouse Experience:** Your spouse gains 1 month of Quebec experience (if applicable).
            * ⚠️ **Age Decay (You & Spouse):** We calculate if you (or your spouse) cross a birthday threshold and deduct points accordingly.
        3.  **Apply Language Target:** We **replace** your current French test results with the level selected on the axis.
        """)

    # --- 5. STRATEGY ANALYSIS ---
    st.markdown("### Strategy Analysis")

    curr_score, audit = scoring.calculate_score(p)

    # Data Pre-processing
    has_vjo_points = audit.get('qn_vjo', 0) > 0
    shortage_score = audit.get('qn_diag', 0)
    has_french_zeros = fr_r_val < 5 or fr_w_val < 5
    spouse_points = audit.get('ad_fr', 0)
    spouse_can_improve = has_spouse and (spouse_points < 40)
    sim_max_score = pivot_df.values.max()

    # Audit Max Constants
    max_age = 100 if has_spouse else 120
    max_edu = 110 if has_spouse else 130
    max_exp = 50 if has_spouse else 70
    max_fr_app = 160 if has_spouse else 200
    max_diag = 120

    full_audit = f"""
    **A. HUMAN CAPITAL ({audit['total_hc']} / 520)**
    - Age: {audit['hc_age']} / {max_age} (Current: {age_val})
    - Education: {audit['hc_edu']} / {max_edu}
    - Career Experience: {audit['hc_exp']} / {max_exp} ({exp_val} months)
    - French (Applicant): {audit['hc_french']} / {max_fr_app} (L:{p.get('fr_l')} S:{p.get('fr_s')} R:{fr_r_val} W:{fr_w_val})

    **B. QUEBEC NEEDS ({audit['total_qn']} / 700)**
    - **Job Shortage:** {shortage_score} / {max_diag} (Diagnosis Points)
    - **Quebec Work History:** {audit['qn_qc_exp']} / 160 ({qc_exp_val} months)
    - **Quebec Diploma:** {audit['qn_dip']} / 200
    - **Validated Job Offer:** {audit['qn_vjo']} / 50 (Locked: {"Yes" if has_vjo_points else "No"})
    - **Regional Ties:** {audit['qn_out']} / 120

    **C. ADAPTATION ({audit['total_ad']} / 180)**
    - Spouse Points: French {audit.get('ad_fr',0)}/40, Age {audit.get('ad_age',0)}/20
    """

    csv_string = pivot_df.to_csv(sep=",")

    # --- REVISED PROMPT: NUANCED ADVISOR ---
    ai_prompt_text = f"""
Act as a Senior Quebec Immigration Strategist.
I am running a simulation to reach a **Target Score of {target_score}. Be concise.

MY TRUTH DATA:
1. Validated Job Offer (VJO): {"YES (+50 pts)" if has_vjo_points else "NO"}
2. Job Shortage Score: {shortage_score} / {max_diag}
3. French Reading/Writing Zeros: {"YES" if has_french_zeros else "NO"}
4. Spouse Potential: {"YES" if spouse_can_improve else "NO"}
5. Simulation Max: {sim_max_score} vs Target: {target_score}

YOUR MISSION: Analyze Risk vs. Reward (Do not be authoritarian) (Max 250 words).
Use a professional, advisory tone. Do not use words like "Forbidden," "Stop," or "Non-negotiable."
Get straight to the point. No fluff. No "I hope this helps."

STRATEGIC ANALYSIS FRAMEWORK:

1. The "Administrative" Trade-off (Job Title/NOC)**
- Scenario: I have a VJO (+50 pts).
- Analysis: Calculate the *Net Impact* of changing my NOC to chase Shortage points.
- Logic: "If you change NOC, you likely lose the VJO (-50) to gain Shortage points (+??). Is Shortage > 50? If not, advise that it is a net loss, but acknowledge it is the user's choice to take that risk."

2. The "Efficiency" Calculation (Language)
- Check Reading/Writing. If Zeros, highlight this as the highest ROI lever (Low Cost / High Points).
- Check Spouse. If they can improve, highlight that even small gains (Level 4) might bridge the gap.

3. The "Structural" Gap (Education)
- **Check:** If [Simulation Max < Target] AND [Language Levers are exhausted].
- **Verdict:** If the math proves I cannot reach the target with Time + French, then (and only then) suggest the Diploma.
- **Tone:** Present it as an investment decision: "To bridge the final X points, you may need to 'buy' structure via a Diploma ($15k+)."

OUTPUT FORMAT:
1. **Strategic Diagnosis:** Review the VJO/Shortage trade-off calmly.
2. **The Efficiency Check:** ROI of Applicant French vs Spouse French.
3. **The Final Plan:** Step-by-step recommendation prioritizing "Free" points before "Expensive" ones.
"""

    encoded_prompt = urllib.parse.quote(ai_prompt_text)
    chatgpt_url = f"https://chatgpt.com/?q={encoded_prompt}"

    col_btn, col_info = st.columns([1, 2])
    with col_btn:
        st.link_button("🚀 Analyze with ChatGPT", chatgpt_url, type="primary")
    with col_info:
        st.caption("Click to open ChatGPT with the **Risk-Calculated Strategy**.")

    with st.expander("Show Raw Prompt (Debug)", expanded=False):
        st.code(ai_prompt_text, language="text")

    st.caption(t("legend"))
