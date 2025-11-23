import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import translations as tr

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
        p_age = st.slider(t("age"), 18, 50, 35)


        # General Experience
        p_gen_exp = st.slider(t("exp"), 0, 60, 36)

        # Education
        edu_display_opts = [get_label(tr.EDU_MAP, k) for k in tr.EDU_MAP.keys()]
        # We need to be careful with index matching when language switches
        # Default to Tech Diploma (index 4) if possible
        p_edu_label = st.selectbox(t("edu"), options=edu_display_opts, index=4)
        p_edu = get_key_from_label(tr.EDU_MAP, p_edu_label)

        st.caption(t("fr_skills"))
        c1, c2 = st.columns(2)
        p_fr_l = c1.number_input(t("list"), 0, 12, 5)
        p_fr_s = c2.number_input(t("speak"), 0, 12, 7)
        p_fr_r = c1.number_input(t("read"), 0, 12, 5)
        p_fr_w = c2.number_input(t("write"), 0, 12, 0)

    with st.expander(t("sec_job"), expanded=False):
        # Diagnosis
        diag_keys = ['None', 'Slight', 'Deficit']
        diag_display = [get_label(tr.DIAG_MAP, k) for k in diag_keys]
        p_diag_label = st.selectbox(t("job_diag"), diag_display, index=0)
        p_diag = get_key_from_label(tr.DIAG_MAP, p_diag_label)

        p_prim_occ = st.slider(t("job_prim_exp"), 0, 60, 12)
        p_qc_exp = st.slider(t("job_qc_exp"), 0, 60, 12)

        # VJO
        vjo_keys = ['None', 'Inside Montreal', 'Outside Montreal']
        vjo_display = [get_label(tr.VJO_MAP, k) for k in vjo_keys]
        p_vjo_label = st.radio(t("vjo"), vjo_display, index=2)
        p_vjo = get_key_from_label(tr.VJO_MAP, p_vjo_label)

        p_auth = st.checkbox(t("auth"))

        # QC Diploma
        qc_keys = ['None', 'PhD', 'Masters', 'Bachelors 3y+', 'Bachelors 2y', 'Tech Diploma 3y', 'Vocational (DEP)']
        qc_dip_display = [get_label(tr.QC_DIP_MAP, k) for k in qc_keys]
        p_qc_dip_label = st.selectbox(t("qc_dip"), qc_dip_display, index=0)
        p_qc_dip = get_key_from_label(tr.QC_DIP_MAP, p_qc_dip_label)

        st.caption(t("reg_ties"))
        p_out_res = st.slider(t("reg_res"), 0, 60, 36)
        p_out_work = st.slider(t("reg_work"), 0, 60, 12)
        p_out_study = st.slider(t("reg_study"), 0, 60, 0)

    with st.expander(t("sec_spouse"), expanded=False):
        p_spouse = st.checkbox(t("sp_check"), value=True)

        if p_spouse:
            col1, col2 = st.columns(2)
            sp_age = col1.slider(t("sp_age"), 18, 50, 35)

            # Spouse Edu
            # Use keys from map to ensure order
            sp_keys = ['PhD', 'Masters', 'Bachelors', 'Tech Diploma', 'High School', 'None']
            sp_edu_display = [get_label(tr.EDU_MAP, k) for k in sp_keys]
            sp_edu_label = col2.selectbox(t("sp_edu"), sp_edu_display, index=1)
            sp_edu = get_key_from_label(tr.EDU_MAP, sp_edu_label)

            sp_qc_exp = st.slider(t("sp_qc_exp"), 0, 60, 12)

            st.caption(t("sp_fr"))
            c1, c2 = st.columns(2)
            sp_l = c1.number_input(t("list"), 0, 12, 0, key="spl")
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

    fr_pts = sum([get_fr_pts(p[k]) for k in ['fr_l', 'fr_s', 'fr_r', 'fr_w']])
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

tab_dash, tab_sim, tab_draws = st.tabs([t("tab_dash"), t("tab_sim"), t("tab_draws")])

# --- TAB 1: DASHBOARD ---
with tab_dash:
    col1, col2, col3 = st.columns(3)
    col1.metric(t("hc"), f"{audit['total_hc']} / 520")
    col2.metric(t("qn"), f"{audit['total_qn']} / 700")
    col3.metric(t("ad"), f"{audit['total_ad']} / 180")

    st.divider()

    color = "green" if total >= 590 else "#d9534f"
    st.markdown(f"""
        <div style="text-align: center; padding: 20px; background-color: {'#e6fffa' if total >= 590 else '#fff5f5'}; border-radius: 10px; margin-bottom: 20px;">
            <h4 style="margin:0; color: #555;">{t('total_score')}</h4>
            <h1 style="margin:0; font-size: 4rem; color: {color};">{total}</h1>
            <p style="margin:0; color: #666;">{t('passing_bench')}</p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander(t("breakdown")):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.write(f"{t('age')}: {audit['hc_age']}")
            st.write(f"{t('edu')}: {audit['hc_edu']}")
            st.write(f"French Language: {audit['hc_french']}")
            st.write(f"Experience General: {audit['hc_exp']}")
        with c2:
            st.write(f"{t('shortage')}: {audit['qn_diag']}")
            st.write(f"Quebec Experience: {audit['qn_qc_exp']}")
            st.write(f"Validated Job Offer: {audit['qn_vjo']}")
            # st.write(f"Reg: {audit['qn_out']}")
            st.write(f"Residence Outside Quebec: {audit['out_res_pts']}")
            st.write(f"Work Outside Quebec: {audit['out_work_pts']}")
            if audit.get('out_study_pts', 0) > 0:
                st.write(f"Study (Region): {audit['out_study_pts']}")
        with c3:
            st.write(f"Spouse French Language: {audit.get('ad_fr', 0)}")
            st.write(f"Spouse Age: {audit.get('ad_age', 0)}")
            st.write(f"Spouse Quebec Experience: {audit.get('ad_exp', 0)}")
            st.write(f"Spouse Education: {audit.get('ad_edu', 0)}")

# --- TAB 3: LATEST DRAWS ---
with tab_draws:
    st.write(f"### {t('draws_title')}")
    st.write(t('draws_sub'))

    draws_df = pd.DataFrame(LATEST_DRAWS)
    st.dataframe(draws_df, width='stretch', hide_index=True)

    st.info(t('tip'))

# --- TAB 2: SIMULATOR ---
with tab_sim:
    st.write(f"### {t('sim_title')}")

    st.markdown(f"#### {t('step1')}")
    draw_options = [t("manual")] + [f"{d['Date']} - {d['Stream']} ({d['Score']} pts)" for d in LATEST_DRAWS]

    c_sel, c_score = st.columns([3, 1])
    target_selection = c_sel.selectbox(t("select_draw"), draw_options, index=0)

    target_score = 600
    if target_selection == t("manual"):
        target_score = c_score.number_input("Target Score", 500, 900, 600)
    else:
        for d in LATEST_DRAWS:
            if f"{d['Date']} - {d['Stream']} ({d['Score']} pts)" == target_selection:
                target_score = d['Score']
                break
        c_score.markdown(f"<div class='target-score-box'>Target<br><b style='font-size:20px'>{target_score}</b></div>", unsafe_allow_html=True)

    st.divider()

    st.markdown(f"#### {t('step2')}")

    # MAPPED INPUT: Simulator Axis Labels
    axis_display_opts = list(tr.AXIS_MAP_LABELS.keys())
    axis_display_labels = [tr.AXIS_MAP_LABELS[k][st.session_state.lang] for k in axis_display_opts]

    col_x, col_y = st.columns(2)
    x_label_sel = col_x.selectbox(t("x_axis"), axis_display_labels, index=0)
    y_label_sel = col_y.selectbox(t("y_axis"), axis_display_labels, index=1)

    x_key = next(k for k, v in tr.AXIS_MAP_LABELS.items() if v[st.session_state.lang] == x_label_sel)
    y_key = next(k for k, v in tr.AXIS_MAP_LABELS.items() if v[st.session_state.lang] == y_label_sel)

    def get_range(k):
        if k == 'time_travel': return [0, 12, 24, 36, 48, 60]
        if 'fr' in k: return [5, 6, 7, 8, 9, 10, 12]
        return []

    x_vals, y_vals = get_range(x_key), get_range(y_key)
    results = []

    for y in y_vals:
        for x in x_vals:
            sim = p.copy()
            def apply_sim(key, val):
                if key == 'time_travel':
                    sim['qc_exp'] += val
                    sim['prim_occ_exp'] += val
                    sim['gen_exp'] += val
                    sim['sp_qc_exp'] += val
                    if sim['out_res'] > 0: sim['out_res'] += val
                    if sim['out_work'] > 0: sim['out_work'] += val
                elif key == 'fr_target':
                    sim['fr_l'] = sim['fr_s'] = sim['fr_r'] = sim['fr_w'] = val
                elif key == 'sp_fr_target':
                    sim['sp_fr_l'] = sim['sp_fr_s'] = sim['sp_fr_r'] = sim['sp_fr_w'] = val
            apply_sim(x_key, x)
            apply_sim(y_key, y)
            s, _ = calculate_score_v10(sim)
            results.append({"x_data": x, "y_data": y, "Score": s})

    df = pd.DataFrame(results)
    pivot_df = df.pivot(index="y_data", columns="x_data", values="Score")
    pivot_df = pivot_df.sort_index(ascending=True)

    text_df = pivot_df.astype(str)

    # --- FIXED COLOR RANGE ---
    # We want a min/max dynamic range for better color sensitivity
    min_score = pivot_df.min().min()
    max_score = pivot_df.max().max()

    # If the user sets a target, we switch to Binary (Red/Green)
    # If no target (or custom mode where user wants to see gradient), we could keep gradient
    # But for "Green Zone Analysis", binary is usually better.
    # To bring back the "Heatmap Gradient" when no specific target is set is tricky because
    # the target defaults to 600.

    # Let's keep your previous "Green Zone" Logic (Binary) which is very useful for planning
    color_df = pivot_df.map(lambda x: 1 if x >= target_score else 0)

    fig = px.imshow(
        color_df,
        text_auto=False,
        aspect="auto",
        color_continuous_scale=["#ef4444", "#22c55e"],
        range_color=[0, 1]
    )

    fig.update_traces(
        text=pivot_df.values,
        texttemplate="%{text}",
        hovertemplate=f"{y_label_sel}: %{{y}}<br>{x_label_sel}: %{{x}}<br><b>Score: %{{text}}</b><extra></extra>"
    )

    fig.update_layout(
        title=dict(text=t("green_zone").format(score=target_score), x=0.5),
        xaxis=dict(type='category', title=x_label_sel, tickmode='array', tickvals=x_vals),
        yaxis=dict(type='category', title=y_label_sel),
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=40, b=0)
    )

    st.plotly_chart(fig, width='stretch')
    st.caption(t("legend"))
