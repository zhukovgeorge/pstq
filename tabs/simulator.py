import streamlit as st
import pandas as pd
import plotly.express as px
import urllib.parse
import translations as tr
from tabs.draws import compute_avg_score
import logic.scoring as scoring

AVG_SCORE = int(round(compute_avg_score(scoring.LATEST_DRAWS)))


def build_hard_rules(stream_name: str) -> str:
    stream_name_lower = stream_name.lower()
    hard_rules = []

    # STREAM 1 – Highly qualified and specialized skills
    if "stream 1" in stream_name_lower:
        hard_rules.append(
            "- STREAM 1 (Highly qualified and specialized skills): You may be eligible "
            "ONLY if ALL of the following are true:\n"
            "  • Your main occupation is classified as FEER 0, 1 or 2.\n"
            "  • You have at least 12 months of full-time or equivalent PAID work "
            "experience in this main occupation, in Québec or outside Québec, within "
            "the last 5 years. Work done as compulsory internships as part of a degree "
            "program can count toward this, but for a maximum of 3 months.\n"
            "  • You have obtained a diploma that directly leads to the practice of a "
            "profession, from a program of at least 1 year of full-time studies (for "
            "example: DEP/ASP, AEC/DEC technical, or a university certificate, minor, "
            "major, bachelor’s, DESS, master’s or doctorate), and this diploma was "
            "obtained BEFORE submitting your application.\n"
            "  • You have French oral knowledge at level 7 or higher (L7/S7+) and "
            "written knowledge at level 5 or higher (W5+) according to the Québec "
            "scale.\n"
            "  • If you have an accompanying spouse, they have spoken French (Speaking and Listening) at level 4 "
            "or higher on the Québec scale.\n"
            "  • If your occupation normally requires a licence to practise in Québec, "
            "you either already hold this licence or can work in a context where the "
            "licence is not required. Otherwise, you belong under Stream 3 (regulated "
            "professions), not Stream 1.\n"
            "If ANY of these conditions are not met, you MUST say I am not eligible for "
            "Stream 1 yet and focus on specific actions to reach the missing thresholds "
            "(e.g. gaining more paid experience, reaching French level 7/5, completing "
            "the required diploma, or resolving licence issues)."
        )

    # STREAM 2 – Intermediate and manual skills
    elif "stream 2" in stream_name_lower:
        hard_rules.append(
            "- STREAM 2 (Intermediate and manual skills): You may be eligible ONLY if "
            "ALL of the following are true:\n"
            "  • Your main occupation is classified as FEER 3, 4 or 5.\n"
            "  • You have at least 24 months (2 years) of PAID full-time or equivalent "
            "work experience in your main occupation within the last 5 years.\n"
            "    - At least 12 months of this experience are in Québec in the main "
            "occupation.\n"
            "    - Up to 12 months may be outside Québec, in your main occupation or in "
            "an occupation in the same broad NOC category (same first digit of the NOC).\n"
            "    - Compulsory internships as part of a degree program can be counted "
            "for a maximum of 3 months. Internships in Québec must be in the main "
            "occupation; internships outside Québec may be in the main occupation or in "
            "an occupation in the same broad NOC category.\n"
            "  • You meet the schooling requirement with at least ONE of the following:\n"
            "    - A diploma equivalent to a Québec high school diploma; OR\n"
            "    - A diploma from a full-time program of at least 1 year that corresponds "
            "in Québec to: a Diploma of Vocational Studies (DEP), an Attestation of "
            "Vocational Specialization (ASP), or an Attestation of College Studies (AEC).\n"
            "    - If your diploma was obtained in Québec: the program is at least "
            "600 hours at secondary level or 900 hours at college level.\n"
            "    - The diploma was obtained BEFORE submitting your application.\n"
            "  • You have spoken French (Speaking and Listening) at level 5 or higher (L5/S5+) on the Québec "
            "scale.\n"
            "  • If you have an accompanying spouse, they have spoken French (Speaking and Listening) at level 4 "
            "or higher on the Québec scale.\n"
            "  • If your occupation normally requires a licence to practise in Québec, "
            "you either already hold this licence or can work in a context where the "
            "licence is not required. Otherwise, you belong under Stream 3 (regulated "
            "professions), not Stream 2.\n"
            "If ANY of these conditions are not met, you MUST say I am not eligible for "
            "Stream 2 yet and prioritize actions to reach the missing thresholds "
            "(e.g. 24 months paid experience with ≥12 in Québec, spoken French (Speaking and Listening) level 5, "
            "and the required diploma)."
        )

    # STREAM 3 – Regulated professions
    elif "stream 3" in stream_name_lower:
        hard_rules.append(
            "- STREAM 3 (Regulated professions): You may be eligible ONLY if ALL of the "
            "following are true:\n"
            "  • Your main occupation is included in the official List of Regulated "
            "Professions of the Ministère.\n"
            "    - If the occupation is FULLY regulated (all associated jobs regulated "
            "in Québec), you MUST go through Stream 3.\n"
            "    - If the occupation is NON-fully regulated (only some associated jobs "
            "are regulated), you may choose Stream 3 or, depending on the FEER "
            "category, Stream 1 or Stream 2.\n"
            "    - If regulation applies only to the professional title (and not the "
            "practice itself), the occupation is NOT considered regulated for Stream 3.\n"
            "    - If regulation applies only in the construction industry, it is "
            "considered regulated ONLY when the job is carried out in that industry.\n"
            "  • You hold at least ONE of the following documents issued by the Québec "
            "regulatory authority governing your profession:\n"
            "    - An authorization (licence) to practise your occupation in Québec "
            "(regular, restrictive, temporary or probationary); OR\n"
            "    - Proof of PARTIAL recognition of equivalence of training or diploma, "
            "dated no more than 5 years before application; OR\n"
            "    - Proof of FULL recognition of equivalence of training or diploma, "
            "dated no more than 5 years before application.\n"
            "    - An acknowledgement of receipt is NOT sufficient.\n"
            "  • You have NOT been refused recognition by the regulatory authority on "
            "the grounds that your qualifications are not recognized for practising "
            "in Québec.\n"
            "  • You meet the French language requirement BASED ON THE FEER CATEGORY "
            "of your occupation:\n"
            "    - If FEER 0, 1 or 2: French oral level 7 or higher (L7/S7+) AND written "
            "level 5 or higher (W5+) according to the Québec scale.\n"
            "    - If FEER 3, 4 or 5: spoken French (Speaking and Listening) level 5 or higher (L5/S5+).\n"
            "  • If you have an accompanying spouse, they have spoken French (Speaking and Listening) at level 4 "
            "or higher on the Québec scale.\n"
            "If ANY of these conditions are not met, you MUST say I am not eligible for "
            "Stream 3 yet and focus on regulatory and/or French-language actions "
            "(e.g. obtaining recognition, increasing French levels according to FEER, "
            "or resolving refusal issues)."
        )

    # Fallback / Manual / Unknown target – summarize all streams
    else:
        # Stream 1 summary
        hard_rules.append(
            "- STREAM 1 (if targeted): Need ALL of the following:\n"
            "  • Main occupation classified FEER 0, 1 or 2.\n"
            "  • ≥12 months of full-time or equivalent PAID work experience in the main "
            "occupation (Québec or outside Québec) within the last 5 years, internships "
            "counting for at most 3 months.\n"
            "  • Diploma leading directly to a profession from a program of ≥1 year full-"
            "time study (DEP/ASP, AEC/DEC technical, university cert/minor/major/"
            "bachelor/DESS/master/PhD), obtained before application.\n"
            "  • French oral L7/S7+ and written W5+; spouse (if any) with spoken "
            "French ≥4.\n"
            "  • Licence conditions satisfied if the occupation is regulated (otherwise "
            "see Stream 3)."
        )

        # Stream 2 summary
        hard_rules.append(
            "- STREAM 2 (if targeted): Need ALL of the following:\n"
            "  • Main occupation classified FEER 3, 4 or 5.\n"
            "  • ≥24 months PAID full-time or equivalent work experience in the last "
            "5 years, with ≥12 months in Québec in the main occupation. Up to 12 months "
            "outside Québec may be in the main occupation or in the same broad NOC "
            "category; internships can count up to 3 months.\n"
            "  • At least a high school diploma OR a ≥1-year full-time program leading "
            "to DEP/ASP/AEC (with Québec programs being ≥600 hours at secondary or "
            "≥900 hours at college level), obtained before application.\n"
            "  • spoken French (Speaking and Listening) L5/S5+; spouse (if any) with spoken French (Speaking and Listening) ≥4.\n"
            "  • Licence conditions satisfied if the occupation is regulated (otherwise "
            "see Stream 3)."
        )

        # Stream 3 summary
        hard_rules.append(
            "- STREAM 3 (if targeted – regulated professions):\n"
            "  • Main occupation appears in the official List of Regulated Professions "
            "of the Ministère (fully or non-fully regulated, with nuances on title-only "
            "or construction-only regulation).\n"
            "  • You hold an authorization to practise OR acceptable partial/full "
            "recognition from the regulatory authority (dated ≤5 years), and you have "
            "not been refused recognition.\n"
            "  • French requirements depend on FEER category: FEER 0–2 → oral 7+, "
            "written 5+; FEER 3–5 → spoken 5+; spouse (if any) spoken 4+."
        )

    hard_rules_text = "\n\n".join(hard_rules)
    return hard_rules_text


def _peq_threshold_met(sim: dict) -> bool:
    """
    Very simplified PEQ-style check (historical, for comparison only):
    - >= 24 months of Quebec work experience
    - French oral level (L/S) >= 7
    """
    def to_int(v):
        try:
            return int(v or 0)
        except Exception:
            return 0

    qc_months = to_int(sim.get("qc_exp", 0))
    fr_l = to_int(sim.get("fr_l", 0))
    fr_s = to_int(sim.get("fr_s", 0))
    oral_level = min(fr_l, fr_s)

    return qc_months >= 24 and oral_level >= 7


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
    st.markdown(t("sim_title_description"))

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
        target_score = c_score.number_input(t("target_score_label"), 500, 900, AVG_SCORE)
        c_score.caption(t("avg_cutoff") + f" ~{AVG_SCORE}")

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

            peq = _peq_threshold_met(sim)

            # SAVE DATA
            results.append({
                "x": x_val,
                "y": y_val,
                "score": score,
                "age": sim.get('age', age_val),   # simulated age
                "date": date_str,                 # simulated date
                "months": months_passed,          # how many months in the future
                "peq": peq,                       # PEQ eligibility flag
            })


    # --- 4. VISUALIZATION ---
    # 1. CREATE DATAFRAME & TEXT
    df_sim = pd.DataFrame(results)

    # By default: label = score as text
    df_sim["score_label"] = df_sim["score"].astype(str)

    # Find the earliest point where PEQ threshold is met
    eligible = df_sim[df_sim["peq"]]

    if not eligible.empty:
        # Row index of earliest eligibility (smallest 'months')
        first_idx = eligible["months"].idxmin()
        # Add a star only there
        df_sim.loc[first_idx, "score_label"] = df_sim.loc[first_idx, "score_label"] + "★"

    # Tooltip text can still mention PEQ status (optional)
    df_sim["peq_text"] = df_sim["peq"].apply(
        lambda v: t("peq_met")
                if v else t("peq_not_met")
    )

    df_sim["tooltip"] = df_sim.apply(
        lambda row: (
            f"<b>{y_label_sel}: {row['y']}</b><br>"
            f"<b>{x_label_sel}: {row['x']}</b><br><br>"
            f"<b>📅 Date: {row.get('date', 'N/A')}</b><br>"
            f"<b>🎂 Age: {row.get('age', 'N/A')}</b><br>"
            f"<b>🏆 Score: {row['score']}</b><br>"
            f"{row['peq_text']}"
        ),
        axis=1
    )



    # 2. PREPARE DATA
    pivot_df = df_sim.pivot(index="y", columns="x", values="score").sort_index()
    p_tooltip = df_sim.pivot(index="y", columns="x", values="tooltip").sort_index()
    p_text = df_sim.pivot(index="y", columns="x", values="score_label").sort_index()


    # 3. COLOR LOGIC (Gradient Red -> Static Green)
    min_val = pivot_df.min().min()
    max_val = pivot_df.max().max()

    # Avoid divide-by-zero
    if max_val == min_val: max_val += 1

    # Case 1: Threshold is ABOVE all observed scores → nobody reaches it → all red
    if target_score > max_val:
        custom_colors = [
            [0.0, "#7f1d1d"],  # Dark red
            [1.0, "#fca5a5"],  # Light red
        ]

    else:
        # Clamp threshold ratio into [0, 1]
        if target_score <= min_val:
            thr_ratio = 0.0
        else:
            thr_ratio = (target_score - min_val) / (max_val - min_val)

        # Below threshold: shades of red
        # At/above threshold: solid green
        custom_colors = [
            [0.0, "#7f1d1d"],                        # Dark red (worst)
            [max(thr_ratio - 1e-6, 0.0), "#fca5a5"], # Light red just before threshold
            [thr_ratio, "#16a34a"],                  # Green exactly at threshold
            [1.0, "#16a34a"],                        # Green above threshold
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
        text=p_text.values,
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
    st.caption(t("legend"))
    st.caption(t("peq_tip"))

        # --- 5. STRATEGY & TIMING ANALYSIS ---
    st.markdown(t("strategy_timing"))

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
        st.success(t("peak_score").format(score=max_score_val))
        st.write(t("peak_score_occurs").format(months=months_to_peak, date=peak_date_str))
        # st.write(f"This occurs in **{months_to_peak} months** ({peak_date_str}).")
    with col_action:
        import pandas as pd
        today = pd.Timestamp.now()
        if isinstance(months_to_peak, (int, float)) and months_to_peak > 3:
            deadline = today + pd.DateOffset(months=months_to_peak - 3)
            st.info(t("lang_test_deadline_label").format(date=deadline.strftime('%b %Y')))
        else:
            st.info(t("lang_test_deadline_asap"))

    if vjo_will_expire:
        st.error(t("vjo_renewal_warning"))

    st.divider()


    # --- 5. EXPLANATION FORMULA ---
    st.markdown(t("calc_section_title"))

    # st.markdown(r"""
    # The simulation recalculates your official score for **every single square** in the grid.
    # It assumes you continue working in your current role:

    # $$
    # \text{Future Score} = \text{Current Profile} + \underbrace{\text{Tenure Gain}}_{\color{green}{\text{Points } \uparrow}} - \underbrace{\text{Age Decay}}_{\color{red}{\text{Points } \downarrow}} + \underbrace{\text{Target French}}_{\color{blue}{\text{New Skill Level}}}
    # $$
    # """)
    st.markdown(t("calc_section_body"))

    with st.expander(t("calc_expander_title")):
        st.markdown(t("calc_section_expander"))



#     st.divider()
#     st.markdown("### 💥 Analysis with AI")
#     # ---------------------------------------------------------
#     # C. PREPARE AI PROMPT
#     # ---------------------------------------------------------

#     # 1. Define Maximums
#     m_age = 100 if has_spouse else 120
#     m_edu = 110 if has_spouse else 130
#     m_exp = 50  if has_spouse else 70
#     m_fr  = 160 if has_spouse else 200
#     m_diag = 120; m_qc = 160; m_vjo = 50; m_reg = 120
#     m_auth = 50
#     m_sp_fr = 40; m_sp_age = 20; m_sp_edu = 20

#     # 2. Glassbox Rules
#     scoring_rules_text = generate_scoring_cheat_sheet(scoring, has_spouse)

#     # 3. Detailed Scorecard
#     detailed_breakdown = f"""
#     [A] HUMAN CAPITAL ({audit.get('total_hc', 0)} / 520)
#     - Age: {audit.get('hc_age', 0)} / {m_age} pts
#     - Education: {audit.get('hc_edu', 0)} / {m_edu} pts
#     - Experience: {audit.get('hc_exp', 0)} / {m_exp} pts ({p.get('gen_exp')} months)
#     - French (Main): {audit.get('hc_french', 0)} / {m_fr} pts
#       (Levels: L{p.get('fr_l')}/S{p.get('fr_s')}/R{p.get('fr_r')}/W{p.get('fr_w')})

#     [B] QUEBEC NEEDS ({audit.get('total_qn', 0)} / 700)
#     - Shortage Job: {audit.get('qn_diag', 0)} / {m_diag} pts
#     - QC Work History: {audit.get('qn_qc_exp', 0)} / {m_qc} pts ({p.get('qc_exp')} months)
#     - VJO (Offer): {audit.get('qn_vjo', 0)} / {m_vjo} pts
#     - Regulated License (Auth): {audit.get('qn_auth', 0)} / {m_auth} pts
#     - Regional Ties: {audit.get('qn_out', 0)} / {m_reg} pts

#     [C] SPOUSE / ADAPTATION ({audit.get('total_ad', 0)} / 180)
#     - Spouse French: {audit.get('ad_fr', 0)} / {m_sp_fr} pts (Levels: L{p.get('sp_fr_l')}/S{p.get('sp_fr_s')})
#     """


#     # 4. Hard eligibility rules by stream (MUST be respected)
#     hard_rules = []
#     hard_rules_text = build_hard_rules(target_stream_name)

#     # 4. Dynamic Instructions (Logic Branching)
#     strategy_instructions = []


#     # [JOB & VJO LOGIC - THE CRITICAL FIX]
#     # We compare the Global Max Projected Score against the Target.
#     # If Max < Target, we stop being conservative and start being aggressive.

#     if audit.get('qn_vjo', 0) == 50:
#         if global_max_projected >= target_score:
#             # SCENARIO A: Safe. The VJO is helping us win. Keep it.
#             strategy_instructions.append("- VJO STATUS: I have a VJO and my projected score meets the target. Emphasize protecting this VJO (do not switch jobs risking it).")
#         else:
#             # SCENARIO B: Stuck. The VJO is not enough. We must switch.
#             strategy_instructions.append("- VJO STATUS: I have a VJO, but my path FAILS even with it (Max Score < Target). Do NOT blindly protect it. I MUST switch to a Shortage Job to bridge the gap. Assume I will secure a new VJO in the new role.")
#             strategy_instructions.append("- STRATEGY CHANGE: Prioritize 'Switching to Shortage NOC' as the #1 Move.")
#     else:
#         # User has no VJO
#         if audit.get('qn_diag', 0) >= 90:
#              strategy_instructions.append("- JOB STATUS: I already have a Deficit Job. Focus on 'Time in Job' and getting a VJO for this job.")
#         else:
#              strategy_instructions.append("- JOB STATUS: My job is not scoring high. Is switching NOCs worth the risk?")
#              strategy_instructions.append("- VJO: I have 0/50. Is getting a VJO the fastest way to get 50 pts?")

#     # [French Logic]
#     strategy_instructions.append("- FRENCH ADVICE: Focus ONLY on big jumps (0 to 5) for me. Do NOT suggest going from 7 to 8 (too much effort, low ROI).")

#     # [License Logic]
#     strategy_instructions.append("- LICENSE CHECK: Only suggest getting a License/Auth if the job is traditionally regulated (Health, Teaching, Engineering). If the job is IT, Tech, or Business, IGNORE this category (assume N/A).")

#     # [Diploma Logic]
#     strategy_instructions.append("- DIPLOMA LOGIC: If you suggest a Diploma, you MUST calculate the Opportunity Cost (Lost Work History points vs Diploma points).")

#     formatted_instructions = "\n".join(strategy_instructions)

#     # 5. Final Prompt
#     ai_prompt_text = f"""
# You are a Senior Quebec immigration lawyer.
# You are NOT my representative; you are giving educational strategy only,
# not legal advice.

# My goal is to reach a Target Score of {target_score} in the PSTQ.
# My current score (today) is {curr_score}.

# The scenario matrix below already encodes all realistic future outcomes
# based on my current profile and the levers we allow (time, French, job, etc.).
# You MUST treat this matrix as the ceiling of what is possible.

# - Current max in the matrix (best case): {max_score_val} pts
# - Global projected maximum across all milestones: {global_max_projected} pts
# - Target stream: {target_stream_name}

# If the global maximum is below the target, you MUST clearly say that I cannot
# reach the target with the allowed levers, and explain which constraint blocks me.

# ------------------------------------------------
# MY DETAILED SCORECARD (Today)
# ------------------------------------------------

# {detailed_breakdown}

# ------------------------------------------------
# FUTURE SCENARIO MATRIX
# (Rows = French level, Cols = Months passed)
# ------------------------------------------------

# Use this text as your only source of future scores:

# {projection_text}

# Do NOT invent new future scores beyond what this matrix implies.

# ------------------------------------------------
# OFFICIAL SCORING REFERENCE (For calculations)
# ------------------------------------------------

# {scoring_rules_text}

# ------------------------------------------------
# HARD ELIGIBILITY RULES BY STREAM (MUST OBEY)
# ------------------------------------------------

# {hard_rules_text}

# Additional hard rules:

# - Never propose a strategy that violates any eligibility rule above.
# - If I do NOT meet the hard rules for the targeted stream, you MUST say
#   that I am not eligible yet, and focus on how to reach eligibility
#   (minimum work months and French).

# ------------------------------------------------
# STRATEGY HEURISTICS (Ruthless ROI)
# ------------------------------------------------

# Use these principles, which come from my own analysis:

# - First, check the Time Only path on my CURRENT job:
#   - State clearly the highest Time-Only score and the month it occurs.
#   - If Time Only never comes close to the target, say that path is dead.

# - High-ROI levers you are allowed to use:
#   - Switching to a Shortage NOC (especially outside Montréal).
#   - Maximizing Shortage NOC points over time (12 / 24 / 36 / 48+ months).
#   - Maximizing Regional ties up to 120/120, especially living/working outside Montréal.
#   - Obtaining a regulated license ONLY if the job is in a traditionally regulated field
#     (health, teaching, engineering, etc.).
#   - Big French jumps only:
#     - Principal: focus on 0 → 5 in Reading/Writing before any micro-upgrades.
#     - Do NOT suggest tiny upgrades like 7 → 8 unless they are numerically decisive.
#     - Spouse: upgrading oral French may add a few points but is secondary.

# - Low or negative ROI levers:
#   - A >900h Quebec diploma often has a high opportunity cost:
#     if it requires stopping work for 12 months, compare the lost work/QC/shortage points
#     to the diploma points. If the net is negative or marginal, say so clearly and
#     do NOT recommend the diploma as a primary strategy.

# - VJO logic:
#   - If I already have a VJO and my projected maximum meets the target, prioritize
#     protecting the current VJO (do not casually suggest risky job changes).
#   - If even with optimal moves my global maximum < target, then acknowledge that
#     protecting the current VJO is not enough, and it may be rational to switch to
#     a Shortage NOC to rebuild a stronger case.

# ------------------------------------------------
# IMPORTANT LIMITATIONS & ASSUMPTIONS (MUST OBEY)
# ------------------------------------------------

# This analysis is a NUMERICAL SIMULATION under a FIXED PROFILE.

# You MUST assume that:
# - The occupation used in this simulation is FIXED and CANNOT be changed.
# - The simulator has ALREADY decided whether the occupation is:
#   - a shortage / deficit occupation or not,
#   - regulated or not,
#   - eligible for license points or not.
# - You are NOT allowed to reclassify the occupation, infer a different NOC,
#   or suggest switching to another profession to increase shortage points.

# Even if I mention a different job title or NOC elsewhere, you MUST treat
# the SCENARIO MATRIX as authoritative and final.

# You do NOT know:
# - My real-life profession or job history;
# - Whether I can realistically switch occupations;
# - Whether another NOC is feasible for me.

# Therefore:
# - Do NOT question, reinterpret, or override the matrix.
# - Do NOT suggest career changes outside what the matrix already encodes.
# - Your task is ONLY to determine whether, by continuing in THIS simulated
#   profile and improving allowed levers (time, French, regional ties,
#   licenses already modeled), the target score is achievable.


# ------------------------------------------------
# YOUR TASK
# ------------------------------------------------

# 1. Use the SCORECARD + MATRIX to decide if the target score {target_score} is
#    realistically reachable under these rules.
# 2. If the global maximum < target, your VERDICT must be NO, and you must explain
#    which bottlenecks cannot be solved (e.g., age, maximum points in Shortage + French).
# 3. If the target IS reachable, identify the simplest high-ROI combo of:
#    - Shortage job tenure,
#    - French jumps,
#    - Regional ties,
#    - License (only if appropriate),
#    that gets me above the target with some buffer, and specify the month.

# ------------------------------------------------
# OUTPUT FORMAT (No intro, no fluff)
# ------------------------------------------------

# 1. THE DIAGNOSIS:
#    - 1–2 sentences. Say whether my current path (without major changes) is dead
#      or still viable, using matrix numbers (e.g. "Time-only peaks at 566 pts in Month 24").

# 2. HIGH-ROI STRATEGY TIMELINE:
#    - Do not just list bullet points. Create a chronological list:
#    - NOW: [Immediate Action] (e.g. Switch to Shortage NOC)
#    - MONTH 12: [Milestone/Status] (e.g. Reach 12m Shortage experience -> +90 pts)
#    - MONTH 18: [Action] (e.g. Take French test, aiming for R5/W5)
#    - MONTH 24: [Result] (Score hits {target_score} -> Target Met)

# 3. VERDICT (YES / NO):
#    - Start the paragraph with YES: or NO:.
#    - If YES: specify the earliest month and score where I exceed {target_score}, and which
#      combo achieves it.
#    - If NO: explain in 2–3 sentences why even the best combo from the matrix fails
#      (e.g. "Even at Month 36 with Shortage + max French + license, the matrix caps at 740 pts.").

# 4. LEGAL DISCLAIMER:
#    - End with one short sentence reminding that this is a numerical simulation only
#      and not legal advice or an official eligibility decision.
# """


#     st.markdown("### Generate AI Strategy")

#     col_copy = st.container()

#     with col_copy:
#         st.info("👇 Recommended: Copy this text and paste it into ChatGPT/Claude.")
#         # st.code automatically provides a copy button on hover
#         st.code(ai_prompt_text, language="markdown")
