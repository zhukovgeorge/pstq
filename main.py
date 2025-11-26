import streamlit as st
import translations as tr
import logic.scoring as scoring

# Import the UI Tabs
from tabs import dashboard, simulator, job_search, draws, french, reference

# ==========================================
# 0. PAGE CONFIG & LANGUAGE INIT
# ==========================================
st.set_page_config(page_title="Quebec PSTQ Calc", layout="wide", initial_sidebar_state="expanded")

if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

# --- HELPER FUNCTIONS ---
def t(key):
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
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 1. SIDEBAR (INPUTS)
# ==========================================
with st.sidebar:
    def update_language():
        st.session_state.lang = 'fr' if st.session_state.lang_choice == "Français" else 'en'

    curr_index = 0 if st.session_state.lang == 'en' else 1
    st.radio(
        label=t("lang_select"),
        options=["English", "Français"],
        index=curr_index,
        horizontal=True,
        key="lang_choice",
        on_change=update_language
    )

    st.divider()
    st.header(t("sb_title"))

    # --- SECTION 1: APPLICANT ---
    with st.expander(t("sec_applicant"), expanded=True):
        p_age = st.slider(t("age"), 18, 50, None)
        p_gen_exp = st.slider(t("exp"), 0, 60, None)

        # Education
        edu_order = [
            'PhD', 'MedSpec', 'Masters 2y', 'Masters 1y', 'Bach 5y', 'Bach 3y',
            'Bach 2y', 'Bach 1y', 'Tech 3y', 'Tech 2y', 'Tech 900h',
            'College Gen', 'DEP 1y', 'DEP 900h', 'DEP 600h', 'HS'
        ]
        edu_display_opts = [get_label(tr.EDU_MAP, k) for k in edu_order]
        p_edu_label = st.selectbox(t("edu"), options=edu_display_opts, index=None)
        p_edu = get_key_from_label(tr.EDU_MAP, p_edu_label)

        st.caption(t("fr_skills"))
        c1, c2 = st.columns(2)
        p_fr_l = c1.number_input(t("list"), 0, 12, 0)
        p_fr_s = c2.number_input(t("speak"), 0, 12, 0)
        p_fr_r = c1.number_input(t("read"), 0, 12, 0)
        p_fr_w = c2.number_input(t("write"), 0, 12, 0)

    # --- SECTION 2: JOB & QUEBEC ---
    with st.expander(t("sec_job"), expanded=False):
        diag_keys = ['None', 'Slight', 'Deficit']
        diag_display = [get_label(tr.DIAG_MAP, k) for k in diag_keys]
        p_diag_label = st.selectbox(t("job_diag"), diag_display, index=0)
        p_diag = get_key_from_label(tr.DIAG_MAP, p_diag_label)

        p_prim_occ = st.slider(t("job_prim_exp"), 0, 60, None)
        p_qc_exp = st.slider(t("job_qc_exp"), 0, 60, None)

        vjo_keys = ['None', 'Inside Montreal', 'Outside Montreal']
        vjo_display = [get_label(tr.VJO_MAP, k) for k in vjo_keys]
        p_vjo_label = st.radio(t("vjo"), vjo_display, index=0)
        p_vjo = get_key_from_label(tr.VJO_MAP, p_vjo_label)

        p_auth = st.checkbox(t("auth"))

        # QC Diploma
        qc_keys = [
            'PhD', 'MedSpec', 'Masters 2y', 'Masters 1y', 'Bach 5y', 'Bach 3y',
            'Bach 2y', 'Bach 1y', 'Tech 3y', 'Tech 900h',
            'College Gen', 'DEP 900h', 'DEP 600h', 'HS', 'None'
        ]
        qc_dip_display = [get_label(tr.QC_DIP_MAP, k) for k in qc_keys]
        p_qc_dip_label = st.selectbox(t("qc_dip"), qc_dip_display, index=14)
        p_qc_dip = get_key_from_label(tr.QC_DIP_MAP, p_qc_dip_label)

        st.caption(t("reg_ties"))
        p_out_res = st.slider(t("reg_res"), 0, 60, None)
        p_out_work = st.slider(t("reg_work"), 0, 60, None)
        p_out_study = st.slider(t("reg_study"), 0, 60, None)

    # --- SECTION 3: SPOUSE ---
    with st.expander(t("sec_spouse"), expanded=False):
        p_spouse = st.checkbox(t("sp_check"), value=False)

        if p_spouse:
            col1, col2 = st.columns(2)
            sp_age = col1.slider(t("sp_age"), 18, 50, None)

            sp_keys = ['PhD', 'Masters', 'Bachelors', 'Tech Diploma', 'High School', 'None']
            sp_edu_display = [get_label(tr.EDU_MAP, k) for k in sp_keys]
            sp_edu_label = col2.selectbox(t("sp_edu"), sp_edu_display, index=None)
            sp_edu = get_key_from_label(tr.EDU_MAP, sp_edu_label)

            sp_qc_exp = st.slider(t("sp_qc_exp"), 0, 60, None)

            st.caption(t("sp_fr"))
            c1, c2 = st.columns(2)
            sp_l = c1.number_input(t("list"), 0, 12, 0, key="spl")
            sp_s = c2.number_input(t("speak"), 0, 12, 0, key="sps")
            sp_r = c1.number_input(t("read"), 0, 12, 0, key="spr")
            sp_w = c2.number_input(t("write"), 0, 12, 0, key="spw")
        else:
            sp_age, sp_edu, sp_qc_exp = 0, 'None', 0
            sp_l, sp_s, sp_r, sp_w = 0,0,0,0

        p_family = st.checkbox(t("fam_check"))

# ==========================================
# 2. STATE & CALCULATION
# ==========================================

profile = {
    'age': p_age, 'edu': p_edu, 'gen_exp': p_gen_exp,
    'fr_l': p_fr_l, 'fr_s': p_fr_s, 'fr_r': p_fr_r, 'fr_w': p_fr_w,
    'diag': p_diag, 'prim_occ_exp': p_prim_occ,
    'qc_exp': p_qc_exp, 'vjo': p_vjo, 'auth': p_auth, 'qc_dip': p_qc_dip,
    'out_res': p_out_res, 'out_work': p_out_work, 'out_study': p_out_study,
    'spouse': p_spouse, 'sp_age': sp_age, 'sp_edu': sp_edu, 'sp_qc_exp': sp_qc_exp,
    'sp_fr_l': sp_l, 'sp_fr_s': sp_s, 'sp_fr_r': sp_r, 'sp_fr_w': sp_w,
    'family': p_family
}

total_score, audit_log = scoring.calculate_score(profile)

# ==========================================
# 3. MAIN CONTENT (TABS)
# ==========================================
st.title(t("app_title"))

t1, t2, t3, t4, t5, t6 = st.tabs([
    t("tab_dash"),
    t("tab_sim"),
    t("tab_job"),
    t("tab_draws"),
    t("tab_lang"),
    t("tab_ref")
])

with t1: dashboard.render(profile, total_score, audit_log, t)
with t2: simulator.render(profile, t, scoring)
with t3: job_search.render()
with t4: draws.render(scoring.LATEST_DRAWS, t)
with t5: french.render(t)
with t6: reference.render(t, scoring, tr)
