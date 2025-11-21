import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# ==========================================
# 0. PAGE CONFIG (Mobile Optimization)
# ==========================================
st.set_page_config(page_title="Quebec PSTQ Calc", layout="wide", initial_sidebar_state="expanded")

# Custom CSS to fix mobile padding
st.markdown("""
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 1rem;}
    div[data-testid="stExpander"] div[role="button"] p {font-size: 1.1rem; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 1. SCORING ENGINE (Your Logic - Unchanged)
# ==========================================

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
    # [YOUR EXISTING CALCULATION LOGIC - COPIED VERBATIM FOR STABILITY]
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

    qn_out = band_points(p['out_res'], OUT_CMM_RES) + band_points(p['out_work'], OUT_CMM_WORK) + band_points(p['out_study'], OUT_CMM_STUDY)
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

# ==========================================
# 2. RESPONSIVE UI
# ==========================================
st.title("🍁 Quebec PSTQ Simulator")
st.markdown("Interactive score calculator for the *Regular Skilled Worker Program*.")

# We use a Sidebar for inputs to keep the main view clean for mobile
with st.sidebar:
    st.header("1. Profile Setup")

    # APPLICANT SECTION
    with st.expander("👤 Applicant (You)", expanded=True):
        col1, col2 = st.columns(2)
        p_age = col1.slider("Age", 18, 50, 35)
        p_edu = col2.selectbox("Education", options=EDU_POINTS_UI.keys(), index=4) # Tech Dip default
        p_gen_exp = st.slider("Total Career Exp (Months)", 0, 60, 36)

        st.caption("French Skills (Level 1-12)")
        c1, c2 = st.columns(2)
        p_fr_l = c1.number_input("Listening", 0, 12, 5)
        p_fr_s = c2.number_input("Speaking", 0, 12, 7)
        p_fr_r = c1.number_input("Reading", 0, 12, 5)
        p_fr_w = c2.number_input("Writing", 0, 12, 0)

    # JOB & TIES SECTION
    with st.expander("💼 Job & Quebec Ties", expanded=False):
        p_diag = st.selectbox("Job Shortage Status", ['None', 'Slight', 'Deficit'], index=0)
        p_prim_occ = st.slider("Exp. in Shortage Job (Months)", 0, 60, 12)
        p_qc_exp = st.slider("Quebec Work History (Months)", 0, 60, 12)

        p_vjo = st.radio("Validated Job Offer", ['None', 'Inside Montreal', 'Outside Montreal'], index=2)
        p_auth = st.checkbox("Professional License (Regulated Job)")
        p_qc_dip = st.selectbox("Quebec Diploma", options=QC_DIPLOMA_POINTS.keys(), index=0)

        st.caption("Regional Ties (Outside Montreal)")
        p_out_res = st.slider("Months Residing", 0, 60, 36)
        p_out_work = st.slider("Months Working", 0, 60, 12)
        p_out_study = st.slider("Months Studying", 0, 60, 0)

    # SPOUSE SECTION
    with st.expander("❤️ Spouse / Partner", expanded=False):
        p_spouse = st.checkbox("Accompanied by Spouse", value=True)

        if p_spouse:
            col1, col2 = st.columns(2)
            sp_age = col1.slider("Spouse Age", 18, 50, 35)
            sp_edu = col2.selectbox("Spouse Edu", options=EDU_SPOUSE_UI.keys(), index=1)
            sp_qc_exp = st.slider("Spouse QC Work (Months)", 0, 60, 12)

            st.caption("Spouse French")
            c1, c2 = st.columns(2)
            sp_l = c1.number_input("Sp. Listen", 0, 12, 0)
            sp_s = c2.number_input("Sp. Speak", 0, 12, 7)
            sp_r = c1.number_input("Sp. Read", 0, 12, 0)
            sp_w = c2.number_input("Sp. Write", 0, 12, 0)
        else:
            # Defaults if no spouse
            sp_age, sp_edu, sp_qc_exp = 0, 'None', 0
            sp_l, sp_s, sp_r, sp_w = 0,0,0,0

        p_family = st.checkbox("Family in QC")

# --- GATHER DATA ---
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
# 3. MAIN DISPLAY (Desktop & Mobile Friendly)
# ==========================================

# SCOREBOARD
col1, col2, col3 = st.columns(3)
col1.metric("Human Capital", f"{audit['total_hc']} / 520")
col2.metric("Quebec Needs", f"{audit['total_qn']} / 700")
col3.metric("Adaptation", f"{audit['total_ad']} / 180")

st.divider()

# BIG TOTAL
pass_mark = 590 if not p_spouse else 620 # Approx cutoffs for visual context
color = "green" if total >= 600 else "red" # Simplified visual check

st.markdown(f"""
    <div style="text-align: center; padding: 20px; background-color: {'#e6fffa' if total >= 600 else '#fff5f5'}; border-radius: 10px; margin-bottom: 20px;">
        <h4 style="margin:0; color: #555;">TOTAL SCORE</h4>
        <h1 style="margin:0; font-size: 3.5rem; color: {color};">{total}</h1>
        <p style="margin:0;">(Targeting ~600+)</p>
    </div>
""", unsafe_allow_html=True)

# DETAILS TAB
tab1, tab2 = st.tabs(["📊 Breakdown", "🔮 Future Simulator"])

with tab1:
    st.write("### Detailed Audit")
    # Convert audit dict to clean table rows
    rows = []
    for k, v in audit.items():
        if isinstance(v, dict): continue # Skip sub-dicts if any
        if "total" in k: continue
        rows.append(f"| {k.replace('_', ' ').upper()} | {v} |")

    # Just showing simple breakdown for mobile readability
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Human Capital**")
        st.write(f"Age: {audit['hc_age']}")
        st.write(f"Edu: {audit['hc_edu']}")
        st.write(f"French: {audit['hc_french']}")
        st.write(f"Exp: {audit['hc_exp']}")
    with c2:
        st.markdown("**Quebec Needs**")
        st.write(f"Shortage: {audit['qn_diag']}")
        st.write(f"QC Exp: {audit['qn_qc_exp']}")
        st.write(f"VJO: {audit['qn_vjo']}")
        st.write(f"Regions: {audit['qn_out']}")
    with c3:
        st.markdown("**Adaptation**")
        st.write(f"Spouse Fr: {audit.get('ad_fr', 0)}")
        st.write(f"Spouse Age: {audit.get('ad_age', 0)}")
        st.write(f"Spouse QC: {audit.get('ad_exp', 0)}")

with tab2:
    st.write("### 🚀 Strategy Simulator")
    st.caption("See how your score changes based on two variables.")

    col_x, col_y = st.columns(2)

    # Simulator Inputs
    x_axis = col_x.selectbox("X-Axis (Bottom)", [('Future Months', 'time_travel'), ('French Skills', 'fr_target')], index=0)
    y_axis = col_y.selectbox("Y-Axis (Left)", [('Future Months', 'time_travel'), ('Spouse French', 'sp_fr_target')], index=1)

    x_key, y_key = x_axis[1], y_axis[1]

    # Define Ranges (You can adjust these step values)
    def get_range(k):
        if k == 'time_travel': return [0, 6, 12, 18, 24, 36] # Added 18 months
        if 'fr' in k: return [4, 5, 6, 7, 8, 9, 10] # Standard TEF levels
        return []

    x_vals = get_range(x_key)
    y_vals = get_range(y_key)

    # Calculate Matrix
    # We use a list of dicts to create a Pandas DataFrame (better for Plotly)
    results = []

    for y in y_vals:
        for x in x_vals:
            sim = p.copy()

            # --- Apply Simulation Logic ---
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

            # Store result
            results.append({
                x_axis[0]: x,
                y_axis[0]: y,
                "Score": s
            })

    # Create DataFrame
    df = pd.DataFrame(results)

    # Pivot data for Heatmap format
    pivot_df = df.pivot(index=y_axis[0], columns=x_axis[0], values="Score")

    # Sort index descending for Y axis so it reads top-to-bottom correctly
    pivot_df = pivot_df.sort_index(ascending=False)

    # --- PLOTLY INTERACTIVE CHART ---
    fig = px.imshow(
        pivot_df,
        text_auto=True,                # Shows the score number in the box
        aspect="auto",                 # Stretches to fit screen
        color_continuous_scale="RdYlGn", # Red to Green color scale
        range_color=[550, 650]         # Min/Max for color logic
    )

    # Clean up the layout
    fig.update_layout(
        title=dict(text="Score Heatmap", x=0.5),
        xaxis_title=x_axis[0],
        yaxis_title=y_axis[0],
        coloraxis_showscale=False      # Hide the color bar to save space on mobile
    )

    # Add tooltips
    fig.update_traces(hovertemplate="%{y}: %{y}<br>%{x}: %{x}<br><b>Score: %{z}</b><extra></extra>")

    st.plotly_chart(fig, use_container_width=True)
