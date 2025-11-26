import streamlit as st
import pandas as pd
import french_utils as fr_calc

def render(t):
    st.header(t("tab4_title"))

    # --- 1. SELECTION ---
    test_type = st.radio(t("sel_test"), ["TEF Canada", "TEFAQ", "TCF Canada"], horizontal=True)
    st.divider()

    # --- 2. CONTEXT ---
    if "TCF" in test_type:
        st.info(f"**{t('ctx_tcf_title')}**\n\n* {t('ctx_tcf_1')}\n* {t('ctx_tcf_2')}\n\n{t('ctx_tcf_warn')}")
    else:
        st.markdown(f"**{t('ctx_tef_title')}**\n\n* {t('ctx_tef_1')}\n* {t('ctx_tef_2')}")

    st.write("")

    col_input, col_res = st.columns([1, 2], gap="large")

    with col_input:
        st.subheader(t("enter_score"))

        # --- INPUTS ---
        sc_l = st.number_input(f"{t('list')} (Compréhension orale)", 0, 699, 0)

        # Speaking
        if "TCF" in test_type:
            label_s = f"{t('speak')} (Scale 0-20)"
            max_s, def_s = 20, 0
        else:
            label_s = f"{t('speak')} (Expression orale)"
            max_s, def_s = 699, 0
        sc_s = st.number_input(label_s, 0, max_s, def_s)

        if test_type == "TEFAQ":
             st.caption(t("tefaq_note"))

        # Reading
        sc_r = st.number_input(f"{t('read')} (Compréhension écrite)", 0, 699, 0)

        # Writing
        if "TCF" in test_type:
            label_w = f"{t('write')} (Scale 0-20)"
            max_w, def_w = 20, 0
        else:
            label_w = f"{t('write')} (Expression écrite)"
            max_w, def_w = 699, 0
        sc_w = st.number_input(label_w, 0, max_w, def_w)

    with col_res:
        # Calculate Bands
        b_l = fr_calc.get_band(test_type, 'Compréhension orale', sc_l)
        b_s = fr_calc.get_band(test_type, 'Expression orale', sc_s)
        b_r = fr_calc.get_band(test_type, 'Compréhension écrite', sc_r)
        b_w = fr_calc.get_band(test_type, 'Expression écrite', sc_w)

        st.subheader(t("results_for").format(test=test_type))
        st.write("")

        # --- HEADERS ---
        h1, h2, h3 = st.columns([1.2, 1, 3.8])
        h1.markdown(f"**{t('col_skill')}**")
        h2.markdown(f"**{t('col_status')}**")
        h3.markdown("**Progress to Next Level**")
        st.markdown("<hr style='margin: 0 0 10px 0; border-top: 1px solid #ddd;'>", unsafe_allow_html=True)

        # --- RENDER ROW ---
        def render_row_clean(label, score, band, skill_name):
            if "TCF" in test_type:
                target, needed, _, floor, max_scale = fr_calc.get_next_threshold_tcf(skill_name, score)
            else:
                target, needed, _, floor = fr_calc.get_next_threshold_tef(score)
                max_scale = 699

            c1, c2, c3 = st.columns([1.2, 1, 3.8])

            with c1:
                st.markdown(f"**{label}**")

            with c2:
                # Simple Badge
                color = "#16a34a" if band >= 7 else "#d97706" if band >= 5 else "#6b7280"
                bg = "#dcfce7" if band >= 7 else "#fef3c7" if band >= 5 else "#f3f4f6"
                border = "#16a34a" if band >= 7 else "#d97706" if band >= 5 else "#e5e7eb"

                if band >= 11: band_name = "C2"
                elif band >= 9: band_name = "C1"
                elif band >= 7: band_name = "B2"
                elif band >= 5: band_name = "B1"
                elif band >= 1: band_name = "A1/A2"
                else: band_name = t("beginner")

                # NO INDENTATION in HTML string
                st.markdown(f"""<div style="background-color:{bg}; color:{color}; padding: 2px 8px; border-radius:4px; display:inline-block; font-weight:bold; font-size:0.9rem; border:1px solid {border}">NCLC {band} <span style="font-weight:normal; font-size:0.8rem">({band_name})</span></div>""", unsafe_allow_html=True)

            with c3:
                # Math
                score_pct = min((score / max_scale) * 100, 100)
                bar_color = "#16a34a" if band >= 7 else "#3b82f6"

                # Logic for Target Line and Helper Text
                if target is not None:
                    target_pct = (target / max_scale) * 100
                    target_line = f'<div style="position:absolute; left:{target_pct}%; top:0; bottom:0; width:2px; background-color:#111827; z-index:5;"></div>'
                    helper_text = f"""<div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#6b7280; margin-top:4px;"><span>Current: <b>{score}</b></span><span style="color:#d97706; font-weight:bold;">+{needed} pts to Level {band+1}</span><span>Target: <b>{target}</b></span></div>"""
                else:
                    target_line = ""
                    helper_text = f"""<div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#6b7280; margin-top:4px;"><span>Current: <b>{score}</b></span><span style="color:#16a34a; font-weight:bold;">Max Level Reached! 🏆</span></div>"""

                # Main Render
                st.markdown(f"""<div style="width:100%; margin-top: 5px;"><div style="width:100%; background-color:#e5e7eb; height:12px; border-radius:6px; position:relative;"><div style="width:{score_pct}%; background-color:{bar_color}; height:100%; border-radius:6px;"></div>{target_line}</div>{helper_text}</div>""", unsafe_allow_html=True)

            st.markdown("<hr style='margin: 8px 0; border-top: 1px solid #f0f0f0;'>", unsafe_allow_html=True)

        render_row_clean(t('list'), sc_l, b_l, 'Compréhension orale')
        render_row_clean(t('speak'), sc_s, b_s, 'Expression orale')
        render_row_clean(t('read'), sc_r, b_r, 'Compréhension écrite')
        render_row_clean(t('write'), sc_w, b_w, 'Expression écrite')
