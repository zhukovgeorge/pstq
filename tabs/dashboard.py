import streamlit as st

def render(p, total, audit, t):
    """
    Renders the Dashboard Tab.
    p: Profile dictionary
    total: Total score (int)
    audit: Audit dictionary (breakdown)
    t: Translation helper function
    """

    # 1. COMPACT SCORE BANNER
    color = "green" if total >= 590 else "#d9534f"
    bg_color = "#e6fffa" if total >= 590 else "#fff5f5"

    st.markdown(f"""
        <div style="text-align: center; padding: 10px; background-color: {bg_color}; border-radius: 8px; margin-bottom: 15px; border: 1px solid {color};">
            <h4 style="margin:0; color: #555; text-transform: uppercase; font-size: 0.85rem;">{t('total_score')}</h4>
            <h1 style="margin: 0; font-size: 3rem; line-height: 1.2; font-weight: 800; color: {color};">{total}</h1>
        </div>
    """, unsafe_allow_html=True)

    # 2. CALCULATE DYNAMIC MAX SCORES (Local logic for display bars)
    is_spouse = p['spouse']

    # Human Capital Max
    m_age = 100 if is_spouse else 120
    m_edu = 110 if is_spouse else 130
    m_exp = 50 if is_spouse else 70
    m_fr_skill = 40 if is_spouse else 50
    m_fr_total = m_fr_skill * 4

    # Quebec Needs Max
    m_diag, m_qc_exp, m_qc_dip = 120, 160, 200
    m_vjo, m_auth = 50, 50
    m_reg_res, m_reg_work, m_reg_study = 40, 60, 20

    # Adaptation Max
    m_sp_fr, m_sp_age, m_sp_exp, m_sp_edu = 40, 20, 30, 20
    m_fam = 10

    # Helper for rows
    def show_row(label, score, max_score, help_key=None):
        val_str = f"**{score}** <span style='color:#999; font-size:0.9em'>/ {max_score}</span>"
        st.markdown(f"{label}: {val_str}", unsafe_allow_html=True, help=t(help_key) if help_key else None)

    # 3. DETAILED COLUMNS
    col_hc, col_qn, col_ad = st.columns(3)

    # --- HUMAN CAPITAL ---
    with col_hc:
        st.markdown(f"### {t('hc')}")
        st.markdown(f"<h3 style='color:#444; margin-top:-10px;'>{audit['total_hc']} <span style='font-size:1rem; color:#888'>/ 520</span></h3>", unsafe_allow_html=True)
        st.markdown("---")

        show_row(t('age'), audit['hc_age'], m_age, 'tip_age')
        show_row(t('edu'), audit['hc_edu'], m_edu, 'tip_edu')
        show_row(t('exp'), audit['hc_exp'], m_exp, 'tip_exp')

        st.markdown(f"<br><b>🗣️ {t('fr_skills')} ({audit['hc_french']} <span style='color:#999; font-size:0.9em'>/ {m_fr_total}</span>)</b>", unsafe_allow_html=True, help=t('tip_fr'))
        st.markdown(f"- {t('list')}: **{audit['fr_l_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)
        st.markdown(f"- {t('speak')}: **{audit['fr_s_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)
        st.markdown(f"- {t('read')}: **{audit['fr_r_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)
        st.markdown(f"- {t('write')}: **{audit['fr_w_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)

    # --- QUEBEC NEEDS ---
    with col_qn:
        st.markdown(f"### {t('qn')}")
        st.markdown(f"<h3 style='color:#444; margin-top:-10px;'>{audit['total_qn']} <span style='font-size:1rem; color:#888'>/ 700</span></h3>", unsafe_allow_html=True)
        st.markdown("---")

        show_row(t('shortage'), audit['qn_diag'], m_diag, 'tip_diag')
        show_row(t('job_qc_exp'), audit['qn_qc_exp'], m_qc_exp, 'tip_qc_exp')
        show_row(t('qc_dip'), audit.get('qn_dip', 0), m_qc_dip, 'tip_qc_dip')
        show_row(t('vjo'), audit['qn_vjo'], m_vjo, 'tip_vjo')
        show_row(t('auth'), audit.get('qn_auth', 0), m_auth, 'tip_auth')

        st.markdown(f"<br><b>📍 {t('reg_ties')}</b>", unsafe_allow_html=True, help=t('tip_reg'))
        show_row(t('reg_res'), audit.get('out_res_pts', 0), m_reg_res, 'tip_reg')
        show_row(t('reg_work'), audit.get('out_work_pts', 0), m_reg_work, 'tip_reg')
        show_row(t('reg_study'), audit.get('out_study_pts', 0), m_reg_study, 'tip_reg')

    # --- ADAPTATION ---
    with col_ad:
        st.markdown(f"### {t('ad')}")
        st.markdown(f"<h3 style='color:#444; margin-top:-10px;'>{audit['total_ad']} <span style='font-size:1rem; color:#888'>/ 180</span></h3>", unsafe_allow_html=True)
        st.markdown("---")

        show_row(t('sp_fr'), audit.get('ad_fr', 0), m_sp_fr, 'tip_sp_gen')
        show_row(t('sp_age'), audit.get('ad_age', 0), m_sp_age, 'tip_sp_gen')
        show_row(t('sp_qc_exp'), audit.get('ad_exp', 0), m_sp_exp, 'tip_sp_gen')
        show_row(t('sp_edu'), audit.get('ad_edu', 0), m_sp_edu, 'tip_sp_gen')
        show_row(t('fam_check'), audit.get('ad_fam', 0), m_fam)
