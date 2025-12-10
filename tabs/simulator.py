import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse
import translations as tr
from tabs.draws import compute_avg_score
import logic.scoring as scoring

AVG_SCORE = int(round(compute_avg_score(scoring.LATEST_DRAWS)))

def generate_scoring_cheat_sheet(scoring, has_spouse):
    """
    Generates a concise, numeric text representation of the scoring grid for the LLM.
    """
    # 1. FRENCH GRID
    if has_spouse:
        fr_txt = (
            "FRENCH (Principal - WITH SPOUSE): "
            "Lvl 5-6: 30pts | Lvl 7-8: 35pts | Lvl 9-10: 38pts. (Jumping 0->5 is +30pts)."
        )
        sp_fr_txt = (
            "FRENCH (Spouse): "
            "Lvl 5-6: 6pts | Lvl 7-8: 8pts | Lvl 9-12: 10pts. (Oral Only)."
        )
        # WITH SPOUSE NUMBERS
        gen_exp_txt = "WORK EXP (General): 12m: 15pts | 24m: 30pts | 36m: 35pts | 48m+: 50pts."
        # Education Gaps (Critical for Strategy)
        edu_txt = (
            "EDUCATION (Spouse Scale): "
            "Masters: 91pts | Bachelors: 87pts | 2-Year Tech: 74pts | High School: 24pts. "
            "(Note: Masters vs Bachelor is only +4pts difference)."
        )
    else:
        fr_txt = (
            "FRENCH (Principal - SINGLE): "
            "Lvl 5-6: 33pts | Lvl 7-8: 39pts | Lvl 9-10: 44pts. (Jumping 0->5 is +33pts)."
        )
        sp_fr_txt = "FRENCH (Spouse): N/A"
        # SINGLE NUMBERS
        gen_exp_txt = "WORK EXP (General): 12m: 30pts | 24m: 60pts | 36m: 70pts | 48m+: 100pts."
        # Education Gaps
        edu_txt = (
            "EDUCATION (Single Scale): "
            "Masters: 104pts | Bachelors: 99pts | 2-Year Tech: 84pts | High School: 38pts. "
            "(Note: Masters vs Bachelor is only +5pts difference)."
        )

    # 2. QUEBEC SPECIFIC HISTORY (Cumulative)
    qc_exp_txt = (
        "QUEBEC WORK HISTORY (Cumulative): "
        "12m: 40pts | 24m: 80pts | 36m: 120pts | 48m+: 160pts. "
        "(This stacks with General Experience)."
    )

    # 3. SHORTAGE (DIAGNOSIS) - PRECISE
    shortage_txt = (
        "SHORTAGE JOB (Deficit Diagnosis): "
        "12m: 90pts | 24m: 100pts | 36m: 110pts | 48m+: 120pts."
    )

    # 4. REGIONAL TIES & OTHER
    # Break down the 120 points so AI sees it scales with time
    misc_txt = (
        "REGIONAL TIES (Outside Montreal): Max 120pts. "
        "Accumulates via Residence (Max 40), Work (Max 60), Study (Max 20). "
        "VJO: Outside MTL = 50pts | Inside MTL = 30pts. "
        "REGULATED LICENSE: Flat 50pts."
    )

    # 5. NUCLEAR OPTION (Diploma)
    dip_txt = "QUEBEC DIPLOMA (>900h trade): Adds approx +60 to +80 pts depending on field."

    return f"{fr_txt}\n{sp_fr_txt}\n{gen_exp_txt}\n{qc_exp_txt}\n{shortage_txt}\n{edu_txt}\n{misc_txt}\n{dip_txt}"

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

    def _draw_label(d: dict) -> str:
        return f"{d['Date']} - {d['Stream']} ({d['Score']} pts)"

    # Only include draws that actually have a numeric score (exclude Stream 4)
    score_draws = [d for d in scoring.LATEST_DRAWS if d["Score"] is not None]

    draw_options = [t("manual")] + [_draw_label(d) for d in score_draws]

    c_sel, c_score = st.columns([3, 1])
    target_selection = c_sel.selectbox(t("select_draw"), draw_options, index=0)

    target_score = AVG_SCORE
    target_stream_name = "Manual Target"

    if target_selection == t("manual"):
        target_score = c_score.number_input("Target Score", 500, 900, AVG_SCORE)
        c_score.caption(f"Average cutoff is ~{AVG_SCORE}")
    else:
        # find the selected draw among score_draws only
        for d in score_draws:
            if _draw_label(d) == target_selection:
                target_score = d["Score"]
                target_stream_name = d["Stream"]
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


# --- 5. STRATEGY & TIMING ANALYSIS ---
    st.markdown("### ⏳ Strategic Timing & Analysis")

    # ---------------------------------------------------------
    # 0. INITIALIZE DATA
    # ---------------------------------------------------------
    curr_score, audit = scoring.calculate_score(p)
    has_spouse = bool(p.get('spouse'))

    # ---------------------------------------------------------
    # A. TIMING CALCULATIONS & PROJECTIONS
    # ---------------------------------------------------------
    max_score_row = df_sim.loc[df_sim['score'].idxmax()]
    max_score_val = max_score_row['score']
    months_to_peak = max_score_row['x']
    peak_date_str = max_score_row.get('date', 'N/A')

    # [NEW] GENERATE FUTURE MATRIX & TRACK GLOBAL MAX
    # We need to know the absolute best possible score (Max Time + Max French)
    # to decide if we should tell the AI to "Protect VJO" or "Burn the Ships".

    milestones = [12, 24, 36, 48, 60]
    projection_lines = []
    global_max_projected = 0 # Track the highest number seen in the matrix

    for m in milestones:
        data_at_m = df_sim[df_sim['x'] == m]
        if not data_at_m.empty:
            low_score = int(data_at_m['score'].min())
            high_score = int(data_at_m['score'].max())

            # Update global max
            if high_score > global_max_projected:
                global_max_projected = high_score

            if low_score == high_score:
                projection_lines.append(f"- Month {m}: Guaranteed {low_score} pts (Time Only)")
            else:
                projection_lines.append(f"- Month {m}: {low_score} pts (Time Only) ...up to... {high_score} pts (Time + Max French)")

    projection_text = "\n".join(projection_lines)

    # Check if the VJO will expire before the peak (18 month validity)
    vjo_will_expire = (audit.get('qn_vjo', 0) == 50) and (months_to_peak > 18)

    # ---------------------------------------------------------
    # B. DISPLAY TIMELINE & WARNINGS
    # ---------------------------------------------------------
    col_peak, col_action = st.columns(2)
    with col_peak:
        st.success(f"**📈 Your Peak Score: {max_score_val}**")
        st.write(f"This occurs in **{months_to_peak} months** ({peak_date_str}).")
    with col_action:
        import pandas as pd
        today = pd.Timestamp.now()
        if isinstance(months_to_peak, (int, float)) and months_to_peak > 3:
            deadline = today + pd.DateOffset(months=months_to_peak - 3)
            st.info(f"**📝 Language Test Deadline: {deadline.strftime('%b %Y')}**")
        else:
            st.info("**📝 Language Test Deadline: ASAP**")

    if vjo_will_expire:
        st.error("⚠️ **Warning:** Your peak score is in >18 months. You will need to renew your VJO.")

    st.divider()

    # ---------------------------------------------------------
    # C. PREPARE AI PROMPT
    # ---------------------------------------------------------

    # 1. Define Maximums
    m_age = 100 if has_spouse else 120
    m_edu = 110 if has_spouse else 130
    m_exp = 50  if has_spouse else 70
    m_fr  = 160 if has_spouse else 200
    m_diag = 120; m_qc = 160; m_vjo = 50; m_reg = 120
    m_auth = 50
    m_sp_fr = 40; m_sp_age = 20; m_sp_edu = 20

    # 2. Glassbox Rules
    scoring_rules_text = generate_scoring_cheat_sheet(scoring, has_spouse)

    # 3. Detailed Scorecard
    detailed_breakdown = f"""
    [A] HUMAN CAPITAL ({audit.get('total_hc', 0)} / 520)
    - Age: {audit.get('hc_age', 0)} / {m_age} pts
    - Education: {audit.get('hc_edu', 0)} / {m_edu} pts
    - Experience: {audit.get('hc_exp', 0)} / {m_exp} pts ({p.get('gen_exp')} months)
    - French (Main): {audit.get('hc_french', 0)} / {m_fr} pts
      (Levels: L{p.get('fr_l')}/S{p.get('fr_s')}/R{p.get('fr_r')}/W{p.get('fr_w')})

    [B] QUEBEC NEEDS ({audit.get('total_qn', 0)} / 700)
    - Shortage Job: {audit.get('qn_diag', 0)} / {m_diag} pts
    - QC Work History: {audit.get('qn_qc_exp', 0)} / {m_qc} pts ({p.get('qc_exp')} months)
    - VJO (Offer): {audit.get('qn_vjo', 0)} / {m_vjo} pts
    - Regulated License (Auth): {audit.get('qn_auth', 0)} / {m_auth} pts
    - Regional Ties: {audit.get('qn_out', 0)} / {m_reg} pts

    [C] SPOUSE / ADAPTATION ({audit.get('total_ad', 0)} / 180)
    - Spouse French: {audit.get('ad_fr', 0)} / {m_sp_fr} pts (Levels: L{p.get('sp_fr_l')}/S{p.get('sp_fr_s')})
    """

    # 4. Dynamic Instructions (Logic Branching)
    strategy_instructions = []

    # [JOB & VJO LOGIC - THE CRITICAL FIX]
    # We compare the Global Max Projected Score against the Target.
    # If Max < Target, we stop being conservative and start being aggressive.

    if audit.get('qn_vjo', 0) == 50:
        if global_max_projected >= target_score:
            # SCENARIO A: Safe. The VJO is helping us win. Keep it.
            strategy_instructions.append("- VJO STATUS: I have a VJO and my projected score meets the target. Emphasize protecting this VJO (do not switch jobs risking it).")
        else:
            # SCENARIO B: Stuck. The VJO is not enough. We must switch.
            strategy_instructions.append("- VJO STATUS: I have a VJO, but my path FAILS even with it (Max Score < Target). Do NOT blindly protect it. I MUST switch to a Shortage Job to bridge the gap. Assume I will secure a new VJO in the new role.")
            strategy_instructions.append("- STRATEGY CHANGE: Prioritize 'Switching to Shortage NOC' as the #1 Move.")
    else:
        # User has no VJO
        if audit.get('qn_diag', 0) >= 90:
             strategy_instructions.append("- JOB STATUS: I already have a Deficit Job. Focus on 'Time in Job' and getting a VJO for this job.")
        else:
             strategy_instructions.append("- JOB STATUS: My job is not scoring high. Is switching NOCs worth the risk?")
             strategy_instructions.append("- VJO: I have 0/50. Is getting a VJO the fastest way to get 50 pts?")

    # [French Logic]
    strategy_instructions.append("- FRENCH ADVICE: Focus ONLY on big jumps (0 to 5) for me. Do NOT suggest going from 7 to 8 (too much effort, low ROI).")

    # [License Logic]
    strategy_instructions.append("- LICENSE CHECK: Only suggest getting a License/Auth if the job is traditionally regulated (Health, Teaching, Engineering). If the job is IT, Tech, or Business, IGNORE this category (assume N/A).")

    # [Diploma Logic]
    strategy_instructions.append("- DIPLOMA LOGIC: If you suggest a Diploma, you MUST calculate the Opportunity Cost (Lost Work History points vs Diploma points).")

    formatted_instructions = "\n".join(strategy_instructions)

    # 5. Final Prompt
    ai_prompt_text = f"""
Act as a Ruthless Quebec Immigration Strategist.
I am running a simulation to reach a Target Score of {target_score}.

Below is my DETAILED SCORECARD.

{detailed_breakdown}

FUTURE SCENARIO MATRIX (Rows = French Level, Cols = Months Passed):
{projection_text}

OFFICIAL SCORING REFERENCE (Use this for math):
{scoring_rules_text}

YOUR INSTRUCTIONS (Follow Strictly):
{formatted_instructions}

OUTPUT FORMAT (No intro, no fluff):
1. THE DIAGNOSIS: Why am I stuck? (1 sentence)
2. THE HIGH-ROI MOVES: List specific actions. Use the FUTURE SCENARIO MATRIX to check if "Time Only" is enough to reach the target.
3. THE VERDICT: Start with "YES" or "NO". Then, summarize the *exact combination* required.
   (Example: "YES: The Matrix shows that Month 24 (Time Only) reaches 780 pts, which exceeds your target. No study needed.")
"""

    encoded_prompt = urllib.parse.quote(ai_prompt_text)
    chatgpt_url = f"https://chatgpt.com/?q={encoded_prompt}"

    col_btn, col_info = st.columns([1, 2])
    with col_btn:
        st.link_button("🚀 Analyze with ChatGPT", chatgpt_url, type="primary")
    with col_info:
        st.caption("Click to open ChatGPT with the **Strict ROI Analysis**.")

    with st.expander("Show Raw Prompt (Debug)", expanded=False):
        st.code(ai_prompt_text, language="text")

    st.caption(t("legend"))
