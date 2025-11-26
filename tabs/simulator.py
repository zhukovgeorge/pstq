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
    axis_display_opts = list(tr.AXIS_MAP_LABELS.keys())
    axis_display_labels = [tr.AXIS_MAP_LABELS[k][st.session_state.lang] for k in axis_display_opts]

    col_x, col_y = st.columns(2)
    x_label_sel = col_x.selectbox(t("x_axis"), axis_display_labels, index=0)
    y_label_sel = col_y.selectbox(t("y_axis"), axis_display_labels, index=1)

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
    for y_val in y_vals:
        for x_val in x_vals:
            sim = p.copy()
            def apply_sim_logic(key, val):
                if key == 'time_travel':
                    years_passed = int(val / 12)
                    sim['age'] = sim['age'] + years_passed
                    if p['spouse']: sim['sp_age'] = sim['sp_age'] + years_passed

                    sim['qc_exp'] += val
                    sim['prim_occ_exp'] += val
                    sim['gen_exp'] += val
                    if p['spouse']: sim['sp_qc_exp'] += val
                    if sim['out_res'] > 0: sim['out_res'] += val
                    if sim['out_work'] > 0: sim['out_work'] += val
                elif key == 'fr_target':
                    sim['fr_l'] = sim['fr_s'] = sim['fr_r'] = sim['fr_w'] = val
                elif key == 'sp_fr_target':
                    sim['sp_fr_l'] = sim['sp_fr_s'] = sim['sp_fr_r'] = sim['sp_fr_w'] = val

            apply_sim_logic(x_key, x_val)
            apply_sim_logic(y_key, y_val)

            score, _ = scoring.calculate_score(sim)
            results.append({"x": x_val, "y": y_val, "score": score})

    # --- 4. VISUALIZATION ---
    df_sim = pd.DataFrame(results)
    pivot_df = df_sim.pivot(index="y", columns="x", values="score")
    pivot_df = pivot_df.sort_index(ascending=False)
    green_zone_df = pivot_df.map(lambda x: 1 if x >= target_score else 0)

    fig = px.imshow(
        green_zone_df, text_auto=False, aspect="auto",
        color_continuous_scale=["#ef4444", "#22c55e"], range_color=[0, 1]
    )

    fig.update_traces(
        text=pivot_df.values,
        texttemplate="%{text}",
        hovertemplate=(f"<b>{y_label_sel}: %{{y}}</b><br><b>{x_label_sel}: %{{x}}</b><br><b>Score: %{{text}}</b><extra></extra>")
    )

    fig.update_layout(
        title=dict(text=t("green_zone").format(score=target_score), x=0.5),
        xaxis=dict(title=x_label_sel, side="bottom", type='category'),
        yaxis=dict(title=y_label_sel, type='category'),
        coloraxis_showscale=False, margin=dict(l=0, r=0, t=40, b=0)
    )

    st.plotly_chart(fig, width='stretch')

    # --- 5. SMART AI PROMPT ---
    st.markdown("### 🤖 Ask AI to Explain")

    curr_score, audit = scoring.calculate_score(p)
    is_sp = p['spouse']

    # Audit Max Constants
    max_age = 100 if is_sp else 120
    max_edu = 110 if is_sp else 130
    max_exp = 50 if is_sp else 70
    max_fr_app = 160 if is_sp else 200

    full_audit = f"""
    **A. HUMAN CAPITAL ({audit['total_hc']} / 520)**
    - Age: {audit['hc_age']} / {max_age} (Current: {p['age']})
    - Education: {audit['hc_edu']} / {max_edu} ({p['edu']})
    - Career Experience: {audit['hc_exp']} / {max_exp} ({p['gen_exp']} months)
    - French (Applicant): {audit['hc_french']} / {max_fr_app} (L:{p['fr_l']} S:{p['fr_s']} R:{p['fr_r']} W:{p['fr_w']})

    **B. QUEBEC NEEDS ({audit['total_qn']} / 700)**
    - **Job Shortage:** {audit['qn_diag']} / 120 (Diagnosis: {p['diag']})
    - **Quebec Work History:** {audit['qn_qc_exp']} / 160 ({p['qc_exp']} months)
    - **Quebec Diploma:** {audit['qn_dip']} / 200 ({p['qc_dip']})
    - **Validated Job Offer:** {audit['qn_vjo']} / 50 ({p['vjo']})
    - **Regional Ties:** {audit['qn_out']} / 120 (Months: {p['out_res']})

    **C. ADAPTATION ({audit['total_ad']} / 180)**
    - Spouse Points: French {audit.get('ad_fr',0)}/40, Age {audit.get('ad_age',0)}/20, QC Work {audit.get('ad_exp',0)}/30
    """

    csv_string = pivot_df.to_csv(sep=",")

    ai_prompt_text = f"""
Act as a Senior Quebec Immigration Strategist.
I am running a simulation to reach a **Target Score of {target_score}** ({target_stream_name}).

Here is my **FULL SCORECARD AUDIT** (Points vs Max Potential):
{full_audit}

Here is my **SIMULATION MATRIX** (X={x_label_sel}, Y={y_label_sel}, Val=Score):
{csv_string}

**YOUR TASK: Find the Missing Points.**
1. **The "Dead End" Check:** If the simulation max < {target_score}, admit the current path fails.
2. **The "Strategic Pivot" (Hidden Levers):** Look at the Audit for zeros. Suggest ONE radical change (e.g. Quebec Diploma/AEC, Job Title Arbitrage, VJO) to bridge the gap.
3. **The Plan:** Summarize Option A (Stay course) vs Option B (Pivot).
"""

    encoded_prompt = urllib.parse.quote(ai_prompt_text)
    chatgpt_url = f"https://chatgpt.com/?q={encoded_prompt}"

    col_btn, col_info = st.columns([1, 2])
    with col_btn:
        st.link_button("🚀 Analyze with ChatGPT", chatgpt_url, type="primary")
    with col_info:
        st.caption("Click to open ChatGPT with your **Full Scorecard** and **Simulation Data**.")

    with st.expander("Show Raw Prompt", expanded=False):
        st.code(ai_prompt_text, language="text")

    st.caption(t("legend"))
