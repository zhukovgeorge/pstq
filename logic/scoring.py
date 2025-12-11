import translations as tr

# --- CONSTANTS (The "Grid") ---

LATEST_DRAWS = [
    {
        "Date": "2025-12-04",
        "Stream": "stream1_label",
        "Score": 781,
        "Invited": 605,
        "Notes": "notes_stream1_diploma",
    },
    {
        "Date": "2025-12-04",
        "Stream": "stream1_label",
        "Score": 644,
        "Invited": 605,
        "Notes": "notes_stream1_manufacturing",
    },

    {
        "Date": "2025-12-04",
        "Stream": "stream2_label",
        "Score": 612,
        "Invited": 604,
        "Notes": "notes_stream2_priority",
    },
    {
        "Date": "2025-12-04",
        "Stream": "stream2_label",
        "Score": 573,
        "Invited": 604,
        "Notes": "notes_stream2_manufacturing",
    },

    {
        "Date": "2025-12-04",
        "Stream": "stream3_label",
        "Score": 717,
        "Invited": 649,
        "Notes": "notes_stream3_priority",
    },
    {
        "Date": "2025-12-04",
        "Stream": "stream3_label",
        "Score": 535,
        "Invited": 649,
        "Notes": "notes_stream3_construction",
    },

    {
        "Date": "2025-08-28",
        "Stream": "stream1_label",
        "Score": 760,
        "Invited": 227,
        "Notes": "notes_stream1_std",
    },
    {
        "Date": "2025-08-14",
        "Stream": "stream3_label",
        "Score": 766,
        "Invited": 277,
        "Notes": "notes_stream3_std",
    },
    {
        "Date": "2025-07-31",
        "Stream": "stream2_label",
        "Score": 661,
        "Invited": 273,
        "Notes": "notes_stream2_std",
    },
    {
        "Date": "2025-07-17",
        "Stream": "stream1_label",
        "Score": 768,
        "Invited": 216,
        "Notes": "notes_stream1_std",
    },

    # Stream 4 – Exceptional talent (no points cutoff)
    {
        "Date": "2025-07-17",
        "Stream": "stream4_label",
        "Score": None,
        "Invited": 22,
        "Notes": "notes_stream4_partner",
    },
    {
        "Date": "2025-08-25",
        "Stream": "stream4_label",
        "Score": None,
        "Invited": 21,
        "Notes": "notes_stream4_exceptional",
    },
    {
        "Date": "2025-12-04",
        "Stream": "stream4_label",
        "Score": None,
        "Invited": 12,
        "Notes": "notes_stream4_doctorate_equiv",
    },
]







DIAG_MATRIX = {
    "None": [(0, 12, 0), (12, 24, 5), (24, 36, 10), (36, 48, 15), (48, 10**9, 25)],
    "Slight": [(0, 12, 0), (12, 24, 70), (24, 36, 80), (36, 48, 90), (48, 10**9, 100)],
    "Deficit": [(0, 12, 0), (12, 24, 90), (24, 36, 100), (36, 48, 110), (48, 10**9, 120)]
}

AGE_SINGLE = {18:110, 19:110, 20:120, 21:120, 22:120, 23:120, 24:120, 25:120, 26:120, 27:120, 28:120, 29:120, 30:120, 31:110, 32:100, 33:90, 34:80, 35:75, 36:70, 37:65, 38:60, 39:55, 40:50, 41:40, 42:30, 43:20, 44:10, 45:0}
AGE_SPOUSE_PA = {18:90, 19:90, 20:100, 21:100, 22:100, 23:100, 24:100, 25:100, 26:100, 27:100, 28:100, 29:100, 30:100, 31:95, 32:90, 33:81, 34:72, 35:68, 36:63, 37:59, 38:54, 39:50, 40:45, 41:36, 42:27, 43:18, 44:9, 45:0}
SP_AGE_ADAPT = {16:18, 17:18, 18:18, 19:18, 20:20, 21:20, 22:20, 23:20, 24:20, 25:20, 26:20, 27:20, 28:20, 29:20, 30:20, 31:18, 32:17, 33:16, 34:15, 35:14, 36:12, 37:10, 38:8, 39:7, 40:6, 41:5, 42:4, 43:3, 44:2, 45:0}

EXP_PA_SINGLE = [(0, 12, 0), (12, 24, 20), (24, 36, 40), (36, 48, 50), (48, 10**9, 70)]
EXP_PA_SPOUSE = [(0, 12, 0), (12, 24, 15), (24, 36, 30), (36, 48, 35), (48, 10**9, 50)]
QC_EXP_PA = [(0, 12, 0), (12, 24, 40), (24, 36, 80), (36, 48, 120), (48, 10**9, 160)]
SP_QC_EXP_TABLE = [(0, 6, 0), (6, 12, 5), (12, 24, 10), (24, 36, 15), (36, 48, 23), (48, 10**9, 30)]

OUT_CMM_RES = [(0, 6, 0), (6, 12, 6), (12, 24, 16), (24, 36, 24), (36, 48, 32), (48, 10**9, 40)]
OUT_CMM_WORK = [(0, 6, 0), (6, 12, 9), (12, 24, 24), (24, 36, 36), (36, 48, 48), (48, 10**9, 60)]
OUT_CMM_STUDY = [(0, 6, 0), (6, 12, 3), (12, 24, 8), (24, 36, 12), (36, 48, 16), (48, 10**9, 20)]

# Updated from our Reference Tab work
EDU_POINTS_UI = {
    'PhD': (130, 110), 'MedSpec': (130, 110), 'Masters 2y': (117, 99), 'Masters 1y': (110, 93),
    'Bach 5y': (110, 93), 'Bach 3y': (104, 88), 'Bach 2y': (91, 77), 'Bach 1y': (78, 66),
    'Tech 3y': (78, 66), 'Tech 2y': (52, 44), 'Tech 900h': (52, 44), 'College Gen': (39, 33),
    'DEP 1y': (26, 22), 'DEP 900h': (26, 22), 'DEP 600h': (13, 11), 'HS': (13, 11)
}

QC_DIPLOMA_POINTS = {
    'PhD': 200, 'MedSpec': 200, 'Masters 2y': 180, 'Masters 1y': 170,
    'Bach 5y': 170, 'Bach 3y': 160, 'Bach 2y': 140, 'Bach 1y': 120,
    'Tech 3y': 120, 'Tech 900h': 80, 'College Gen': 60,
    'DEP 900h': 40, 'DEP 600h': 20, 'HS': 20, 'None': 0
}

EDU_SPOUSE_UI = {'PhD': 20, 'Masters': 18, 'Bachelors': 16, 'Tech Diploma': 12, 'High School': 2, 'None': 0}

# --- CALCULATION ENGINE ---

def band_points(months, bands):
    for lo, hi, pts in bands:
        if lo <= months < hi: return pts
    return 0

def calculate_score(p):
    """
    Core Scoring Engine.
    Input: 'p' dictionary (profile).
    Output: (Total Score, Audit Dictionary).
    """
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

    # Age
    age_table = AGE_SPOUSE_PA if spouse else AGE_SINGLE
    # Handle ages > 45 safely
    hc_age = age_table.get(p['age'], 0)
    audit['hc_age'] = hc_age
    hc += hc_age

    # Experience
    hc_exp = band_points(p['gen_exp'], EXP_PA_SPOUSE if spouse else EXP_PA_SINGLE)
    audit['hc_exp'] = hc_exp
    hc += hc_exp

    # Education
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

        # Spouse Age
        sp_age_pts = SP_AGE_ADAPT.get(p['sp_age'], 0)
        audit['ad_age'] = sp_age_pts
        ad += sp_age_pts

        # Spouse QC Work
        sp_qc_pts = band_points(p['sp_qc_exp'], SP_QC_EXP_TABLE)
        audit['ad_exp'] = sp_qc_pts
        ad += sp_qc_pts

        # Spouse Edu
        sp_edu_pts = EDU_SPOUSE_UI.get(p['sp_edu'], 0)
        audit['ad_edu'] = sp_edu_pts
        ad += sp_edu_pts

    final_ad = min(ad, 180)
    audit['total_ad'] = final_ad

    return final_hc + final_qn + final_ad, audit
