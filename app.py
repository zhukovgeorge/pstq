import streamlit as st
import pandas as pd
import plotly.express as px
import translations as tr
import french_utils as fr_calc
import urllib.parse
import job_data

# ==========================================
# 0. PAGE CONFIG & LANGUAGE INIT
# ==========================================
st.set_page_config(page_title="Quebec PSTQ Calc", layout="wide", initial_sidebar_state="expanded")

# Initialize Language Session State
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

# --- HELPER FUNCTIONS ---
def t(key):
    """Fetch text based on current language"""
    return tr.TEXTS[st.session_state.lang].get(key, key)

def get_label(category_map, key):
    return category_map.get(key, {}).get(st.session_state.lang, key)

def get_key_from_label(category_map, label):
    for key, langs in category_map.items():
        if langs.get(st.session_state.lang) == label:
            return key
    return label

# --- CSS ---
st.markdown("""
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 1rem;}
    div[data-testid="stExpander"] div[role="button"] p {font-size: 1.1rem; font-weight: bold;}

    /* COMPACT TARGET BOX */
    .target-score-box {
        background-color: #f0fdf4;
        border: 1px solid #16a34a;
        color: #14532d;            /* Dark Green Text */
        padding: 15px;         /* 5px Top/Bottom, 10px Left/Right */
        border-radius: 6px;
        text-align: center;
        line-height: 1.1;          /* Tighter lines */
        font-size: 0.9rem;         /* Base font smaller */
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 1. SIDEBAR (WITH CALLBACK FIX)
# ==========================================
with st.sidebar:
    # --- CALLBACK FUNCTION ---
    # This function runs immediately when the user clicks the button,
    # BEFORE the rest of the app reloads.
    def update_language():
        if st.session_state.lang_choice == "Français":
            st.session_state.lang = 'fr'
        else:
            st.session_state.lang = 'en'

    # Determine current index for the widget
    curr_index = 0 if st.session_state.lang == 'en' else 1

    # --- LANGUAGE WIDGET ---
    st.radio(
        label=t("lang_select"),
        options=["English", "Français"],
        index=curr_index,
        horizontal=True,
        key="lang_choice",       # We give it a key to access it in the callback
        on_change=update_language # <--- THIS IS THE FIX
    )

    st.divider()

    # --- REST OF SIDEBAR ---
    st.header(t("sb_title"))

    with st.expander(t("sec_applicant"), expanded=True):
        # Age
        p_age = st.slider(t("age"), 18, 50, 36)


        # General Experience
        p_gen_exp = st.slider(t("exp"), 0, 60, 24)

        # Education
        edu_display_opts = [get_label(tr.EDU_MAP, k) for k in tr.EDU_MAP.keys()]
        # We need to be careful with index matching when language switches
        # Default to Tech Diploma (index 4) if possible
        p_edu_label = st.selectbox(t("edu"), options=edu_display_opts, index=1)
        p_edu = get_key_from_label(tr.EDU_MAP, p_edu_label)

        st.caption(t("fr_skills"))
        c1, c2 = st.columns(2)
        p_fr_l = c1.number_input(t("list"), 0, 12, 7)
        p_fr_s = c2.number_input(t("speak"), 0, 12, 7)
        p_fr_r = c1.number_input(t("read"), 0, 12, 0)
        p_fr_w = c2.number_input(t("write"), 0, 12, 0)

    with st.expander(t("sec_job"), expanded=False):
        # Diagnosis
        diag_keys = ['None', 'Slight', 'Deficit']
        diag_display = [get_label(tr.DIAG_MAP, k) for k in diag_keys]
        p_diag_label = st.selectbox(t("job_diag"), diag_display, index=0)
        p_diag = get_key_from_label(tr.DIAG_MAP, p_diag_label)

        p_prim_occ = st.slider(t("job_prim_exp"), 0, 60, 24)
        p_qc_exp = st.slider(t("job_qc_exp"), 0, 60, 24)

        # VJO
        vjo_keys = ['None', 'Inside Montreal', 'Outside Montreal']
        vjo_display = [get_label(tr.VJO_MAP, k) for k in vjo_keys]
        p_vjo_label = st.radio(t("vjo"), vjo_display, index=0)
        p_vjo = get_key_from_label(tr.VJO_MAP, p_vjo_label)

        p_auth = st.checkbox(t("auth"))

        # QC Diploma
        qc_keys = ['None', 'PhD', 'Masters', 'Bachelors 3y+', 'Bachelors 2y', 'Tech Diploma 3y', 'Vocational (DEP)']
        qc_dip_display = [get_label(tr.QC_DIP_MAP, k) for k in qc_keys]
        p_qc_dip_label = st.selectbox(t("qc_dip"), qc_dip_display, index=0)
        p_qc_dip = get_key_from_label(tr.QC_DIP_MAP, p_qc_dip_label)

        st.caption(t("reg_ties"))
        p_out_res = st.slider(t("reg_res"), 0, 60, 36)
        p_out_work = st.slider(t("reg_work"), 0, 60, 24)
        p_out_study = st.slider(t("reg_study"), 0, 60, 0)

    with st.expander(t("sec_spouse"), expanded=False):
        p_spouse = st.checkbox(t("sp_check"), value=True)

        if p_spouse:
            col1, col2 = st.columns(2)
            sp_age = col1.slider(t("sp_age"), 18, 50, 38)

            # Spouse Edu
            # Use keys from map to ensure order
            sp_keys = ['PhD', 'Masters', 'Bachelors', 'Tech Diploma', 'High School', 'None']
            sp_edu_display = [get_label(tr.EDU_MAP, k) for k in sp_keys]
            sp_edu_label = col2.selectbox(t("sp_edu"), sp_edu_display, index=3)
            sp_edu = get_key_from_label(tr.EDU_MAP, sp_edu_label)

            sp_qc_exp = st.slider(t("sp_qc_exp"), 0, 60, 24)

            st.caption(t("sp_fr"))
            c1, c2 = st.columns(2)
            sp_l = c1.number_input(t("list"), 0, 12, 7, key="spl")
            sp_s = c2.number_input(t("speak"), 0, 12, 7, key="sps")
            sp_r = c1.number_input(t("read"), 0, 12, 0, key="spr")
            sp_w = c2.number_input(t("write"), 0, 12, 0, key="spw")
        else:
            sp_age, sp_edu, sp_qc_exp = 0, 'None', 0
            sp_l, sp_s, sp_r, sp_w = 0,0,0,0

        p_family = st.checkbox(t("fam_check"))

# ==========================================
# 2. MAIN TITLE (Renders instantly correct now)
# ==========================================
st.title(t("app_title"))

# ==========================================
# 3. DATA & CONSTANTS
# ==========================================

LATEST_DRAWS = [
    {"Date": "2025-08-25", "Stream": "Stream 1 (Highly qualified and specialized skills)", "Score": 768, "Invited": 216},
    {"Date": "2025-08-14", "Stream": "Stream 3 (Regulated professions)", "Score": 766, "Invited": 275},
    {"Date": "2025-07-31", "Stream": "Stream 2 (Intermediate and manual skills)", "Score": 661, "Invited": 273},
    {"Date": "2025-07-28", "Stream": "Stream 1 (Highly qualified and specialized skills)", "Score": 760, "Invited": 227},
]

DIAG_MATRIX = {
    "None": [(0, 12, 0), (12, 24, 5), (24, 36, 10), (36, 48, 15), (48, 10**9, 25)],
    "Slight": [(0, 12, 0), (12, 24, 70), (24, 36, 80), (36, 48, 90), (48, 10**9, 100)],
    "Deficit": [(0, 12, 0), (12, 24, 90), (24, 36, 100), (36, 48, 110), (48, 10**9, 120)]
}

AGE_SINGLE = {18:110, 19:110, 20:120, 21:120, 22:120, 23:120, 24:120, 25:120, 26:120, 27:120, 28:120, 29:120, 30:120, 31:110, 32:100, 33:90, 34:80, 35:75, 36:70, 37:65, 38:60, 39:55, 40:50, 41:40, 42:30, 43:20, 44:10}
AGE_SPOUSE_PA = {18:90, 19:90, 20:100, 21:100, 22:100, 23:100, 24:100, 25:100, 26:100, 27:100, 28:100, 29:100, 30:100, 31:95, 32:90, 33:81, 34:72, 35:68, 36:63, 37:59, 38:54, 39:50, 40:45, 41:36, 42:27, 43:18, 44:9}
SP_AGE_ADAPT = {16:18, 17:18, 18:18, 19:18, 20:20, 21:20, 22:20, 23:20, 24:20, 25:20, 26:20, 27:20, 28:20, 29:20, 30:20, 31:18, 32:17, 33:16, 34:15, 35:14, 36:12, 37:10, 38:8, 39:7, 40:6, 41:5, 42:4, 43:3, 44:2}

EXP_PA_SINGLE = [(0, 12, 0), (12, 24, 20), (24, 36, 40), (36, 48, 50), (48, 10**9, 70)]
EXP_PA_SPOUSE = [(0, 12, 0), (12, 24, 15), (24, 36, 30), (36, 48, 35), (48, 10**9, 50)]
QC_EXP_PA = [(0, 12, 0), (12, 24, 40), (24, 36, 80), (36, 48, 120), (48, 10**9, 160)]
SP_QC_EXP_TABLE = [(0, 6, 0), (6, 12, 5), (12, 24, 10), (24, 36, 15), (36, 48, 23), (48, 10**9, 30)]

OUT_CMM_RES = [(0, 6, 0), (6, 12, 6), (12, 24, 16), (24, 36, 24), (36, 48, 32), (48, 10**9, 40)]
OUT_CMM_WORK = [(0, 6, 0), (6, 12, 9), (12, 24, 24), (24, 36, 36), (36, 48, 48), (48, 10**9, 60)]
OUT_CMM_STUDY = [(0, 6, 0), (6, 12, 3), (12, 24, 8), (24, 36, 12), (36, 48, 16), (48, 10**9, 20)]

EDU_POINTS_UI = {'PhD': (130, 110), 'Masters': (117, 99), 'Bachelors 3y+': (104, 88), 'Bachelors 2y': (91, 77), 'Tech Diploma 3y': (78, 66), 'High School': (13, 11)}
QC_DIPLOMA_POINTS = {'None': 0, 'PhD': 200, 'Masters': 180, 'Bachelors 3y+': 160, 'Bachelors 2y': 140, 'Tech Diploma 3y': 120, 'Vocational (DEP)': 60}
EDU_SPOUSE_UI = {'PhD': 20, 'Masters': 18, 'Bachelors': 16, 'Tech Diploma': 12, 'High School': 2, 'None': 0}

def band_points(months, bands):
    for lo, hi, pts in bands:
        if lo <= months < hi: return pts
    return 0

def calculate_score_v10(p):
    audit = {}
    spouse = p['spouse']

    # --- 1. HUMAN CAPITAL ---
    hc = 0
    def get_fr_pts(lvl):
        if lvl >= 9: return 40 if spouse else 50
        if lvl >= 7: return 35 if spouse else 44
        if lvl >= 5: return 30 if spouse else 38
        return 0

    p_fr_l = get_fr_pts(p['fr_l'])
    p_fr_s = get_fr_pts(p['fr_s'])
    p_fr_r = get_fr_pts(p['fr_r'])
    p_fr_w = get_fr_pts(p['fr_w'])

    audit['fr_l_pts'] = p_fr_l
    audit['fr_s_pts'] = p_fr_s
    audit['fr_r_pts'] = p_fr_r
    audit['fr_w_pts'] = p_fr_w

    fr_pts = p_fr_l + p_fr_s + p_fr_r + p_fr_w
    audit['hc_french'] = fr_pts
    hc += fr_pts

    hc_age = (AGE_SPOUSE_PA if spouse else AGE_SINGLE).get(p['age'], 0)
    audit['hc_age'] = hc_age
    hc += hc_age

    hc_exp = band_points(p['gen_exp'], EXP_PA_SPOUSE if spouse else EXP_PA_SINGLE)
    audit['hc_exp'] = hc_exp
    hc += hc_exp

    hc_edu = EDU_POINTS_UI.get(p['edu'], (0,0))[1 if spouse else 0]
    audit['hc_edu'] = hc_edu
    hc += hc_edu

    final_hc = min(hc, 520)
    audit['total_hc'] = final_hc

    # --- 2. QUEBEC NEEDS ---
    qn = 0
    qn_diag = band_points(p['prim_occ_exp'], DIAG_MATRIX.get(p['diag'], []))
    audit['qn_diag'] = qn_diag
    qn += qn_diag

    qn_qc_exp = band_points(p['qc_exp'], QC_EXP_PA)
    audit['qn_qc_exp'] = qn_qc_exp
    qn += qn_qc_exp

    qn_dip = QC_DIPLOMA_POINTS.get(p['qc_dip'], 0)
    audit['qn_dip'] = qn_dip
    qn += qn_dip

    pts_out_res = band_points(p['out_res'], OUT_CMM_RES)
    pts_out_work = band_points(p['out_work'], OUT_CMM_WORK)
    pts_out_study = band_points(p['out_study'], OUT_CMM_STUDY)

    audit['out_res_pts'] = pts_out_res
    audit['out_work_pts'] = pts_out_work
    audit['out_study_pts'] = pts_out_study

    qn_out = pts_out_res + pts_out_work + pts_out_study
    audit['qn_out'] = qn_out
    qn += qn_out

    qn_vjo = 50 if p['vjo'] == 'Outside Montreal' else (30 if p['vjo'] == 'Inside Montreal' else 0)
    audit['qn_vjo'] = qn_vjo
    qn += qn_vjo

    qn_auth = 50 if p['auth'] else 0
    audit['qn_auth'] = qn_auth
    qn += qn_auth

    final_qn = min(qn, 700)
    audit['total_qn'] = final_qn

    # --- 3. ADAPTATION ---
    ad = 0
    ad_fam = 10 if p['family'] else 0
    audit['ad_fam'] = ad_fam
    ad += ad_fam

    if spouse:
        def get_sp_fr_pts(lvl):
            if lvl >= 9: return 10
            if lvl >= 7: return 8
            if lvl >= 5: return 6
            if lvl == 4: return 4
            return 0
        sp_fr = sum([get_sp_fr_pts(p[k]) for k in ['sp_fr_l', 'sp_fr_s', 'sp_fr_r', 'sp_fr_w']])
        audit['ad_fr'] = sp_fr
        ad += sp_fr

        sp_age_pts = SP_AGE_ADAPT.get(p['sp_age'], 0)
        audit['ad_age'] = sp_age_pts
        ad += sp_age_pts

        sp_qc_pts = band_points(p['sp_qc_exp'], SP_QC_EXP_TABLE)
        audit['ad_exp'] = sp_qc_pts
        ad += sp_qc_pts

        sp_edu_pts = EDU_SPOUSE_UI.get(p['sp_edu'], 0)
        audit['ad_edu'] = sp_edu_pts
        ad += sp_edu_pts

    final_ad = min(ad, 180)
    audit['total_ad'] = final_ad

    return final_hc + final_qn + final_ad, audit

# Gather data
p = {
    'age': p_age, 'edu': p_edu, 'gen_exp': p_gen_exp,
    'fr_l': p_fr_l, 'fr_s': p_fr_s, 'fr_r': p_fr_r, 'fr_w': p_fr_w,
    'diag': p_diag, 'prim_occ_exp': p_prim_occ,
    'qc_exp': p_qc_exp, 'vjo': p_vjo, 'auth': p_auth, 'qc_dip': p_qc_dip,
    'out_res': p_out_res, 'out_work': p_out_work, 'out_study': p_out_study,
    'spouse': p_spouse, 'sp_age': sp_age, 'sp_edu': sp_edu, 'sp_qc_exp': sp_qc_exp,
    'sp_fr_l': sp_l, 'sp_fr_s': sp_s, 'sp_fr_r': sp_r, 'sp_fr_w': sp_w,
    'family': p_family
}

total, audit = calculate_score_v10(p)

# ==========================================
# 4. MAIN TABS
# ==========================================

tab_dash, tab_sim, tab_job, tab_draws, tab_lang, tab_ref = st.tabs([
    t("tab_dash"),
    t("tab_sim"),
    t("tab_job"),
    t("tab_draws"),
    t("tab_lang"),
    t("tab_ref")
])

# --- TAB 1: DASHBOARD ---
with tab_dash:
    # 1. COMPACT SCORE BANNER
    color = "green" if total >= 590 else "#d9534f"
    bg_color = "#e6fffa" if total >= 590 else "#fff5f5"

    st.markdown(f"""
        <div style="text-align: center; padding: 10px; background-color: {bg_color}; border-radius: 8px; margin-bottom: 15px; border: 1px solid {color};">
            <h4 style="margin:0; color: #555; text-transform: uppercase; font-size: 0.85rem;">{t('total_score')}</h4>
            <h1 style="margin: 0; font-size: 3rem; line-height: 1.2; font-weight: 800; color: {color};">{total}</h1>
            <p style="margin:0; color: #666; font-size: 0.8rem;">{t('passing_bench')}</p>
        </div>
    """, unsafe_allow_html=True)

    # 2. CALCULATE DYNAMIC MAX SCORES (Single vs Spouse)
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

    # HELPER FUNCTION FOR DISPLAYING ROWS WITH TOOLTIPS
    def show_row(label, score, max_score, help_key=None):
        # Format: "**Score** / Max"
        val_str = f"**{score}** <span style='color:#999; font-size:0.9em'>/ {max_score}</span>"

        # Render Markdown with the 'help' parameter
        st.markdown(
            f"{label}: {val_str}",
            unsafe_allow_html=True,
            help=t(help_key) if help_key else None
        )

    # 3. DETAILED BREAKDOWN COLUMNS
    col_hc, col_qn, col_ad = st.columns(3)

    # --- GROUP 1: HUMAN CAPITAL (Max 520) ---
    with col_hc:
        st.markdown(f"### {t('hc')}")
        st.markdown(f"<h3 style='color:#444; margin-top:-10px;'>{audit['total_hc']} <span style='font-size:1rem; color:#888'>/ 520</span></h3>", unsafe_allow_html=True)
        st.markdown("---")

        # Pass the 'tip_...' keys here as the 4th argument
        show_row(t('age'), audit['hc_age'], m_age, 'tip_age')
        show_row(t('edu'), audit['hc_edu'], m_edu, 'tip_edu')
        show_row(t('exp'), audit['hc_exp'], m_exp, 'tip_exp')

        # French (Exploded View)
        st.markdown(f"<br><b>🗣️ {t('fr_skills')} ({audit['hc_french']} <span style='color:#999; font-size:0.9em'>/ {m_fr_total}</span>)</b>", unsafe_allow_html=True, help=t('tip_fr'))
        st.markdown(f"- {t('list')}: **{audit['fr_l_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)
        st.markdown(f"- {t('speak')}: **{audit['fr_s_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)
        st.markdown(f"- {t('read')}: **{audit['fr_r_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)
        st.markdown(f"- {t('write')}: **{audit['fr_w_pts']}** <span style='color:#aaa'>/ {m_fr_skill}</span>", unsafe_allow_html=True)

    # --- GROUP 2: QUEBEC NEEDS (Max 700) ---
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

    # --- GROUP 3: ADAPTATION (Max 180) ---
    with col_ad:
        st.markdown(f"### {t('ad')}")
        st.markdown(f"<h3 style='color:#444; margin-top:-10px;'>{audit['total_ad']} <span style='font-size:1rem; color:#888'>/ 180</span></h3>", unsafe_allow_html=True)
        st.markdown("---")

        show_row(t('sp_fr'), audit.get('ad_fr', 0), m_sp_fr, 'tip_sp_gen')
        show_row(t('sp_age'), audit.get('ad_age', 0), m_sp_age, 'tip_sp_gen')
        show_row(t('sp_qc_exp'), audit.get('ad_exp', 0), m_sp_exp, 'tip_sp_gen')
        show_row(t('sp_edu'), audit.get('ad_edu', 0), m_sp_edu, 'tip_sp_gen')
        show_row(t('fam_check'), audit.get('ad_fam', 0), m_fam)

# --- TAB 4: LATEST DRAWS ---
with tab_draws:
    st.write(f"### {t('draws_title')}")
    st.write(t('draws_sub'))

    draws_df = pd.DataFrame(LATEST_DRAWS)
    st.dataframe(draws_df, width='content', hide_index=True)

    st.info(t('tip'))

# --- TAB 2: SIMULATOR ---
import urllib.parse

with tab_sim:
    st.header(t("sim_title"))
    st.markdown("""
    This tool simulates how your score changes over time.
    **Crucial:** It accounts for **Age Decay**. As you gain experience (points up), you also get older (points down).
    """)

    # --- 1. TARGET SELECTION ---
    st.subheader(t("step1"))

    draw_options = [t("manual")] + [f"{d['Date']} - {d['Stream']} ({d['Score']} pts)" for d in LATEST_DRAWS]

    c_sel, c_score = st.columns([3, 1])
    target_selection = c_sel.selectbox(t("select_draw"), draw_options, index=0)

    target_score = 600
    target_stream_name = "Manual Target"

    if target_selection == t("manual"):
        target_score = c_score.number_input("Target Score", 500, 900, 600)
    else:
        for d in LATEST_DRAWS:
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
                    # Age Decay Logic
                    years_passed = int(val / 12)
                    sim['age'] = sim['age'] + years_passed
                    if p['spouse']:
                        sim['sp_age'] = sim['sp_age'] + years_passed

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

            score, _ = calculate_score_v10(sim)
            results.append({"x": x_val, "y": y_val, "score": score})

    # --- 4. VISUALIZATION ---
    df_sim = pd.DataFrame(results)
    pivot_df = df_sim.pivot(index="y", columns="x", values="score")
    pivot_df = pivot_df.sort_index(ascending=True)
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

    # --- 5. SMART AI PROMPT (FULL GAP ANALYSIS) ---
    st.markdown("### 🤖 Ask AI to Explain")

    # A. Calculate Current Snapshot
    curr_score, audit = calculate_score_v10(p)

    # B. Define Max Points (Constants for "Headroom" calculation)
    # Using 'is_spouse' to adjust max values
    is_sp = p['spouse']
    max_age = 100 if is_sp else 120
    max_edu = 110 if is_sp else 130
    max_exp = 50 if is_sp else 70
    max_fr_app = 160 if is_sp else 200 # Total French points

    max_diag = 120
    max_qc_exp = 160
    max_qc_dip = 200
    max_vjo = 50
    max_reg = 120 # Res+Work+Study

    # C. Build the "Full Picture" Audit String
    full_audit = f"""
    **A. HUMAN CAPITAL ({audit['total_hc']} / 520)**
    - Age: {audit['hc_age']} / {max_age} (Current: {p['age']})
    - Education: {audit['hc_edu']} / {max_edu} ({p['edu']})
    - Career Experience: {audit['hc_exp']} / {max_exp} ({p['gen_exp']} months)
    - French (Applicant): {audit['hc_french']} / {max_fr_app} (L:{p['fr_l']} S:{p['fr_s']} R:{p['fr_r']} W:{p['fr_w']})

    **B. QUEBEC NEEDS ({audit['total_qn']} / 700)**
    - **Job Shortage:** {audit['qn_diag']} / {max_diag} (Diagnosis: {p['diag']})
    - **Quebec Work History:** {audit['qn_qc_exp']} / {max_qc_exp} ({p['qc_exp']} months)
    - **Quebec Diploma:** {audit['qn_dip']} / {max_qc_dip} ({p['qc_dip']})
    - **Validated Job Offer:** {audit['qn_vjo']} / {max_vjo} ({p['vjo']})
    - **Regional Ties:** {audit['qn_out']} / {max_reg} (Months: {p['out_res']})

    **C. ADAPTATION ({audit['total_ad']} / 180)**
    - Spouse French: {audit.get('ad_fr',0)} / 40
    - Spouse Age: {audit.get('ad_age',0)} / 20
    - Spouse QC Work: {audit.get('ad_exp',0)} / 30
    - Spouse Edu: {audit.get('ad_edu',0)} / 20
    """

    csv_string = pivot_df.to_csv(sep=",")

    # D. The "Strategic Pivot" Prompt
    ai_prompt_text = f"""
Act as a Senior Quebec Immigration Strategist.
I am running a simulation to reach a **Target Score of {target_score}** ({target_stream_name}).

Here is my **FULL SCORECARD AUDIT** (Points vs Max Potential):
{full_audit}

Here is my **SIMULATION MATRIX** (X={x_label_sel}, Y={y_label_sel}):
{csv_string}

**YOUR TASK: Find the Missing Points.**
Don't just analyze the matrix. Look at the "Scorecard Audit" for zeros or low scores.

**1. The "Dead End" Check:**
Look at the Simulation Matrix. If the maximum score < {target_score}, admit that the current path is insufficient.

**2. The "Strategic Pivot" (Hidden Levers):**
If the simulation fails, look at the Audit above and suggest ONE radical change to bridge the gap.
- **Is Job Shortage 0/120?** Ask: "Can you switch to a shortage field (IT, Construction, Health)?"
- **Is Quebec Diploma 0/200?** Ask: "Can you take a 1-year AEC program? That is worth +60-90 points."
- **Is Regional Ties 0/120?** Ask: "Can you move 50km outside Montreal?"
- **Is Spouse French low?** Ask: "Can your spouse reach Level 7?"

**3. The Plan:**
Provide a summary: "Option A: Stay the course (if matrix works)" OR "Option B: The Pivot (if matrix fails)."
"""

    # E. Magic Link
    encoded_prompt = urllib.parse.quote(ai_prompt_text)
    chatgpt_url = f"https://chatgpt.com/?q={encoded_prompt}"

    col_btn, col_info = st.columns([1, 2])
    with col_btn:
        st.link_button("🚀 Analyze with ChatGPT", chatgpt_url, type="primary")
    with col_info:
        st.caption("Click to open ChatGPT with your **Full Scorecard Audit** and **Simulation Data**.")

    with st.expander("Show Raw Prompt", expanded=False):
        st.code(ai_prompt_text, language="text")

    st.caption(t("legend"))

# --- TAB 5: FRENCH BAND CALCULATOR ---
with tab_lang:
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
                # IMPORTANT: Strings are flattened to one line to avoid indentation errors
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


# ==========================================
# TAB 3: JOB SHORTAGE SEARCH (Fixed Styling)
# ==========================================

with tab_job:
    st.header("🕵️ Job Market Intelligence")
    st.markdown("""
    **Goal:** Identify if your profession is in **Deficit** (High Points).
    *Data Source: Official Govt. Diagnostics*
    """)

    # --- 1. LOAD DATA ---
    df_jobs = pd.DataFrame(job_data.JOBS)

    # --- 2. DASHBOARD STATS ---
    deficit_count = len(df_jobs[df_jobs['Diagnosis'].str.contains("Déficit", na=False)])
    st.metric("Total Deficit Professions", deficit_count, delta="High Priority Targets")

    st.divider()

    # --- 3. SEARCH & FILTERS ---
    col_search, col_cat, col_diag = st.columns([2, 1, 1])

    search_txt = col_search.text_input("🔍 Search Job Title or NOC", placeholder="e.g. Software, 21232")

    cat_opts = ["All"] + sorted(df_jobs['Category'].unique().tolist())
    sel_cat = col_cat.selectbox("Category", cat_opts)

    diag_opts = ["All"] + sorted(df_jobs['Diagnosis'].dropna().unique().tolist())
    sel_diag = col_diag.selectbox("Diagnosis", diag_opts)

    # Apply Filters
    filtered = df_jobs.copy()

    if search_txt:
        mask = filtered.astype(str).apply(lambda x: x.str.contains(search_txt, case=False, na=False)).any(axis=1)
        filtered = filtered[mask]

    if sel_cat != "All":
        filtered = filtered[filtered['Category'] == sel_cat]

    if sel_diag != "All":
        filtered = filtered[filtered['Diagnosis'] == sel_diag]

    # --- 4. DISPLAY TABLE (Standard Theme) ---
    st.write(f"Showing **{len(filtered)}** matches:")

    # We use standard Streamlit rendering which automatically handles Dark/Light mode
    st.dataframe(
        filtered,
        width='stretch',
        column_config={
            "NOC": st.column_config.TextColumn("Code", width="small"),
            "Title": "Job Title",
            "Diagnosis": st.column_config.TextColumn("Status", width="medium"),
            "Category": st.column_config.TextColumn("Sector", width="medium"),
        },
        hide_index=True
    )

    # --- 5. VISUAL ANALYSIS ---
    if not filtered.empty:
        with st.expander("📊 View Category Analysis", expanded=False):
            cat_counts = filtered['Category'].value_counts().reset_index()
            cat_counts.columns = ['Category', 'Count']

            fig = px.bar(
                cat_counts,
                x='Count',
                y='Category',
                orientation='h',
                title="Distribution of Jobs by Category (Filtered)",
                color='Count',
                color_continuous_scale="viridis" # Standard professional scale
            )
            st.plotly_chart(fig, width='stretch')


# ==========================================
# TAB 5: OFFICIAL SCORING REFERENCE (Vertical Layout)
# ==========================================
with tab_ref:
    st.header("📚 Official Scoring Grids (PSTQ)")
    st.markdown("""
    This reference section details the exact point allocation used by the Ministry of Immigration (MIFI).
    Use these tables to verify your score calculation manually.
    """)

    grid_cat = st.radio(
        "Select Category to Explore:",
        ["1. Human Capital (Age, Edu, French)", "2. Quebec Labor Needs (Work, VJO)", "3. Spouse & Adaptation"],
        horizontal=True
    )

    st.divider()

    # --- CATEGORY 1: HUMAN CAPITAL ---
    if "1." in grid_cat:
        # 1. AGE SECTION
        st.subheader("📅 1. Age Points")
        st.caption("Points are maximized from age 18 to 30, then decrease by ~5 points per year.")

        age_data = []
        for age in range(18, 46):
            age_data.append({
                "Age": str(age) if age < 45 else "45+",
                "Single Applicant": AGE_SINGLE.get(age, 0),
                "With Spouse": AGE_SPOUSE_PA.get(age, 0)
            })
        st.dataframe(pd.DataFrame(age_data), hide_index=True, width='stretch')

        st.divider()

        # 2. EDUCATION SECTION
        st.subheader("🎓 2. Education Points")
        st.caption("Points based on the highest obtained diploma.")

        edu_data = []
        for key, val in EDU_POINTS_UI.items():
            edu_data.append({
                "Diploma Level": get_label(tr.EDU_MAP, key),
                "Single": val[0],
                "With Spouse": val[1]
            })
        st.dataframe(pd.DataFrame(edu_data), hide_index=True, width='stretch')

        st.divider()

        # 3. FRENCH SECTION
        st.subheader("🗣️ 3. French Proficiency (Principal Applicant)")
        st.caption("Points are awarded per skill. **Level 7 (B2)** is the major threshold.")

        fr_data = [
            {"NCLC Level": "Level 1-4 (Beginner)", "Points (per skill)": "0"},
            {"NCLC Level": "Level 5-6 (Low B1)", "Points (Single)": "38", "Points (Spouse)": "30"},
            {"NCLC Level": "Level 7-8 (B2)", "Points (Single)": "44", "Points (Spouse)": "35"},
            {"NCLC Level": "Level 9-12 (C1/C2)", "Points (Single)": "50", "Points (Spouse)": "40"},
        ]
        st.table(pd.DataFrame(fr_data))
        st.info("**Note:** Total French Score = Sum of all 4 skills. Max possible is 200 (Single) or 160 (With Spouse).")

    # --- CATEGORY 2: QUEBEC NEEDS ---
    elif "2." in grid_cat:
        # 1. WORK EXPERIENCE
        st.subheader("💼 1. Work Experience")
        st.caption("Points are awarded based on cumulative full-time work experience in the last 5 years.")

        exp_data = []
        for band in EXP_PA_SINGLE:
            label = f"{band[0]} to {band[1]-1} months"
            if band[1] > 1000: label = "48+ months"

            sp_val = 0
            for sb in EXP_PA_SPOUSE:
                if sb[0] == band[0]: sp_val = sb[2]

            exp_data.append({
                "Duration": label,
                "General Experience": band[2],
                "Gen. Exp (With Spouse)": sp_val,
            })
        st.dataframe(pd.DataFrame(exp_data), hide_index=True, width='stretch')

        st.divider()

        # 2. JOB SHORTAGE
        st.subheader("🏥 2. Job Shortage Diagnosis")
        st.caption("Bonus points if your occupation is on the Deficit list.")
        diag_data = [
            {"Diagnosis": "Deficit (Déficitaire)", "Points": "Max (Up to 120)"},
            {"Diagnosis": "Slight Deficit (Léger)", "Points": "Medium"},
            {"Diagnosis": "Balanced (Équilibré)", "Points": "0"},
        ]
        st.table(pd.DataFrame(diag_data))

        st.divider()

        # 3. QUEBEC SPECIFICS
        st.subheader("⚜️ 3. Quebec Specifics")
        qc_data = [
            {"Factor": "Validated Job Offer (Montreal)", "Points": "30"},
            {"Factor": "Validated Job Offer (Outside MTL)", "Points": "50"},
            {"Factor": "Quebec Diploma (Tech/Univ)", "Points": "Up to 60-90"},
            {"Factor": "Regional Ties (Living >2 years)", "Points": "Up to 120"},
        ]
        st.dataframe(pd.DataFrame(qc_data), hide_index=True, width='stretch')

    # --- CATEGORY 3: SPOUSE ---
    elif "3." in grid_cat:
        st.subheader("❤️ Spouse / Common-Law Partner Factors")
        st.markdown("If you apply with a spouse, the total score denominator changes. The spouse contributes points to the total.")

        st.divider()

        st.markdown("#### 1. Spouse Education")
        sp_edu_data = [{"Level": k, "Points": v} for k, v in EDU_SPOUSE_UI.items()]
        st.dataframe(pd.DataFrame(sp_edu_data), hide_index=True, width='stretch')

        st.divider()

        st.markdown("#### 2. Spouse Age")
        sp_age_data = [{"Age": str(k), "Points": v} for k, v in SP_AGE_ADAPT.items() if k % 2 == 0]
        st.dataframe(pd.DataFrame(sp_age_data), hide_index=True, width='stretch')

        st.divider()

        st.markdown("#### 3. Spouse French (Oral Only)")
        st.caption("Spouse points are usually awarded for Listening and Speaking only.")
        sp_fr_data = [
            {"Level": "Level 1-4", "Points": "0"},
            {"Level": "Level 5-6", "Points": "6"},
            {"Level": "Level 7-8", "Points": "8"},
            {"Level": "Level 9+", "Points": "10"},
        ]
        st.table(pd.DataFrame(sp_fr_data))

        st.divider()

        st.markdown("#### 4. Spouse Quebec Work")
        sp_qc_data = []
        for band in SP_QC_EXP_TABLE:
            label = f"{band[0]} to {band[1]-1} months"
            if band[1] > 1000: label = "48+ months"
            sp_qc_data.append({"Duration": label, "Points": band[2]})
        st.dataframe(pd.DataFrame(sp_qc_data), hide_index=True, width='stretch')
