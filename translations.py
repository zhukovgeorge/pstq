# translations.py

# ==========================================
# 1. MAPPINGS FOR LOGIC-HEAVY INPUTS
# ==========================================

EDU_MAP = {
    'PhD': {'en': 'PhD (Univ 3rd Cycle)', 'fr': 'Doctorat (3e cycle)'},
    'MedSpec': {'en': 'Medicine/Dentistry/Optometry (Master/PhD level)', 'fr': 'Médecine/Dentisterie/Optométrie'},
    'Masters 2y': {'en': 'Masters (2 years+)', 'fr': 'Maîtrise (2 ans+)'},
    'Masters 1y': {'en': 'Masters (1 year)', 'fr': 'Maîtrise (1 an)'},
    'Bach 5y': {'en': 'Bachelors (5 years+)', 'fr': 'Baccalauréat (5 ans+)'},
    'Bach 3y': {'en': 'Bachelors (3-4 years)', 'fr': 'Baccalauréat (3-4 ans)'},
    'Bach 2y': {'en': 'Bachelors (2 years)', 'fr': 'Baccalauréat (2 ans)'},
    'Bach 1y': {'en': 'Univ 1st Cycle (1 year)', 'fr': 'Univ 1er cycle (1 an)'},
    'Tech 3y': {'en': 'College Technical (3 years / DEC)', 'fr': 'Collégial technique (3 ans)'},
    'Tech 2y': {'en': 'College Technical (1-2 years)', 'fr': 'Collégial technique (1-2 ans)'},
    'Tech 900h': {'en': 'College Technical (900h+ / AEC)', 'fr': 'Collégial technique (900h+ / AEC)'},
    'College Gen': {'en': 'College General (2 years)', 'fr': 'Collégial préuniversitaire (2 ans)'},
    'DEP 1y': {'en': 'Vocational (1 year+ outside QC)', 'fr': 'Secondaire prof. (1 an+ hors QC)'},
    'DEP 900h': {'en': 'Vocational (DEP 900h+)', 'fr': 'DEP (900h+)'},
    'DEP 600h': {'en': 'Vocational (DEP 600-899h)', 'fr': 'DEP (600-899h)'},
    'HS': {'en': 'High School (General)', 'fr': 'Secondaire général'}
}

DIAG_MAP = {
    "None": {"en": "None", "fr": "Aucun"},
    "Slight": {"en": "Slight", "fr": "Léger (Slight)"},
    "Deficit": {"en": "Deficit", "fr": "Déficitaire (Deficit)"}
}

VJO_MAP = {
    "None": {"en": "None", "fr": "Aucune"},
    "Inside Montreal": {"en": "Inside Montreal", "fr": "Dans Montréal (CMM)"},
    "Outside Montreal": {"en": "Outside Montreal", "fr": "Hors Montréal"}
}

QC_DIP_MAP = {
    'PhD': {'en': 'PhD', 'fr': 'Doctorat'},
    'MedSpec': {'en': 'Medicine/Dentistry (2y+)', 'fr': 'Médecine/Dentisterie (2 ans+)'},
    'Masters 2y': {'en': 'Masters (2 years+)', 'fr': 'Maîtrise (2 ans+)'},
    'Masters 1y': {'en': 'Masters (1 year)', 'fr': 'Maîtrise (1 an)'},
    'Bach 5y': {'en': 'Bachelors (5 years+)', 'fr': 'Baccalauréat (5 ans+)'},
    'Bach 3y': {'en': 'Bachelors (3-4 years)', 'fr': 'Baccalauréat (3-4 ans)'},
    'Bach 2y': {'en': 'Bachelors (2 years)', 'fr': 'Baccalauréat (2 ans)'},
    'Bach 1y': {'en': 'Univ 1st Cycle (1 year)', 'fr': 'Univ 1er cycle (1 an)'},
    'Tech 3y': {'en': 'Tech DEC (3 years)', 'fr': 'DEC Technique (3 ans)'},
    'Tech 900h': {'en': 'AEC (>900h) / Tech (>900h)', 'fr': 'AEC (>900h) / Technique'},
    'College Gen': {'en': 'Pre-University DEC (2 years)', 'fr': 'DEC Préuniversitaire'},
    'DEP 900h': {'en': 'DEP (>900h)', 'fr': 'DEP (>900h)'},
    'DEP 600h': {'en': 'DEP (600-899h)', 'fr': 'DEP (600-899h)'},
    'HS': {'en': 'High School (DES)', 'fr': 'Secondaire général (DES)'},
    'None': {'en': 'None', 'fr': 'Aucun'}
}

AXIS_MAP_LABELS = {
    "time_travel": {"en": "Future Months Worked", "fr": "Mois Travaillés (Futur)"},
    "fr_target": {"en": "My French Target (All Skills)", "fr": "Cible Français (Moi)"},
    "sp_fr_target": {"en": "Spouse French Target (All Skills)", "fr": "Cible Français (Conjoint)"}
}

JOB_DIAG_VALUE_MAP = {
    # note: exact accents + lowercase "déficit" / "surplus"
    "Déficit":        {"en": "Deficit",        "fr": "Déficit"},
    "Léger déficit":  {"en": "Slight deficit", "fr": "Léger déficit"},
    "Équilibre":      {"en": "Balanced",       "fr": "Équilibre"},
    "Léger surplus":  {"en": "Slight surplus", "fr": "Léger surplus"},
    "Surplus":        {"en": "Surplus",        "fr": "Surplus"},
    "Non publié":     {"en": "Not published",  "fr": "Non publié"},
}


# translations.py

JOB_CAT_VALUE_MAP = {
    "Legislative and senior management occupations": {
        "en": "Legislative and senior management occupations",
        "fr": "Professions législatives et de haute direction",
    },
    "Business, finance and administration occupations": {
        "en": "Business, finance and administration occupations",
        "fr": "Professions en affaires, finance et administration",
    },
    "Natural and applied sciences and related occupations": {
        "en": "Natural and applied sciences and related occupations",
        "fr": "Professions en sciences naturelles et appliquées et domaines connexes",
    },
    "Health occupations": {
        "en": "Health occupations",
        "fr": "Professions des soins de santé",
    },
    "Occupations in education, law and social, community and government services": {
        "en": "Occupations in education, law and social, community and government services",
        "fr": "Professions en éducation, droit, services sociaux, communautaires et gouvernementaux",
    },
    "Occupations in art, culture, recreation and sport": {
        "en": "Occupations in art, culture, recreation and sport",
        "fr": "Professions dans les arts, la culture, les loisirs et les sports",
    },
    "Sales and service occupations": {
        "en": "Sales and service occupations",
        "fr": "Professions en vente et services",
    },
    "Trades, transport and equipment operators and related occupations": {
        "en": "Trades, transport and equipment operators and related occupations",
        "fr": "Métiers, transport, opérateurs d’équipement et professions connexes",
    },
    "Natural resources, agriculture and related production occupations": {
        "en": "Natural resources, agriculture and related production occupations",
        "fr": "Professions des ressources naturelles, de l’agriculture et de la production connexe",
    },
    "Occupations in manufacturing and utilities": {
        "en": "Occupations in manufacturing and utilities",
        "fr": "Professions de la fabrication et des services publics",
    },
}


# ==========================================
# 2. GENERAL UI TEXT
# ==========================================

TEXTS = {
    "en": {
        "app_title": "🍁 Quebec PSTQ Simulator",
        "app_subtitle": "Interactive score calculator for the *Regular Skilled Worker Program*.",
        "lang_select": "Langue / Language",

        # Sidebar
        "sb_title": "1. Profile Setup",
        "sec_applicant": "👤 Applicant (You)",
        "sec_job": "💼 Job & Quebec Ties",
        "sec_spouse": "❤️ Spouse / Partner",
        "age": "Age",
        "edu": "Education",
        "exp": "Total Career Exp (Months)",
        "fr_skills": "French Skills (Quebec scale Level 1-12)",
        "list": "Listening",
        "speak": "Speaking",
        "read": "Reading",
        "write": "Writing",

        "job_diag": "Job Shortage Status",
        "job_prim_exp": "Exp. in Shortage Job (Months)",
        "job_qc_exp": "Quebec Work History (Months)",
        "vjo": "Validated Job Offer",
        "auth": "Professional License (Regulated Job)",
        "qc_dip": "Quebec Diploma",
        "reg_ties": "Regional Ties (Outside Montreal)",
        "reg_res": "Months Residing",
        "reg_work": "Months Working",
        "reg_study": "Months Studying",

        "sp_check": "Accompanied by Spouse",
        "sp_age": "Spouse Age",
        "sp_edu": "Spouse Edu",
        "sp_qc_exp": "Spouse QC Work (Months)",
        "sp_fr": "Spouse French",
        "fam_check": "Family in QC",

        # Tabs
        "tab_dash": "📊 Dashboard",
        "tab_sim": "🚀 Strategy Simulator",
        "tab_draws": "📜 Latest Draws",
        "tab_lang": "🌐 French Converter",
        "tab_job": "🕵️ Job Search",
        "tab_ref": "📚 Official Scoring Grids",
        "tab_contact": "📬 Contact",

        # Job Search Tab
                # Job Search Tab
        "job_subheader": (
            "**Goal:** Identify if your profession is in **Deficit** (High Points).\n"
            "*Data Source: Official Govt. Diagnostics*"
        ),
        "job_search_placeholder": "e.g. Software, 21232",
        "job_filter_category": "Category",
        "job_filter_diagnosis": "Diagnosis",

        "job_col_noc": "NOC Code",
        "job_col_title": "Job Title",
        "job_col_diag": "Diagnosis",
        "job_col_cat": "Category",
        "job_stats_deficit": "Total Deficit Professions",
        "job_stats_deficit_delta": "High Priority Targets",
        "job_stats_slight_deficit" : "Total Slight Deficit Professions",
        "job_stats_slight_deficit_delta": "Moderate Priority Targets",
        "job_matches": "Showing **{n}** matches:",
        "job_cat_chart_title": "Distribution of Jobs by Category (Filtered)",

        # Dashboard
        "hc": "Human Capital",
        "qn": "Quebec Needs",
        "ad": "Adaptation",
        "total_score": "TOTAL SCORE",
        "breakdown": "See Detailed Point Breakdown",
        "shortage": "Shortage",

        # Simulator
        "sim_title": "🎯 Target Strategy Map",
        "sim_title_description": "This tool simulates how your score changes over time. Crucial: It accounts for Age Decay. As you gain experience (points up), you also get older (points down).",
        "step1": "Step 1: Set your Target",
        "select_draw": "Select a Draw Round to Beat:",
        "manual": "Manual Entry",
        "step2": "Step 2: Simulate Future Scenarios",
        "x_axis": "X-Axis (Bottom)",
        "y_axis": "Y-Axis (Left)",
        "green_zone": "Green Zone Analysis (Cutoff: {score})",
        "legend": "🟥 Red = Score below threshold | 🟩 Green = Score ≥ threshold",
        "avg_cutoff": "Average Cutoff is",
        "peq_tip": "💡 **Tip:** A cell marked with a star ★ indicates a point where a simplified PEQ-style threshold (≥24 months of Quebec work + French oral ≥7) would be met.",
        "strategy_timing": "### ⏳ Strategic Timing & Analysis",
        "peq_met": "✅ PEQ threshold met (historical program)",
        "peq_not_met": "❌ PEQ threshold not met",
        "peak_score": "📈 Your Peak Score: {score}",
        "peak_score_occurs" : "This occurs in **{months} months** ({date}).",
        "lang_test_deadline_label" : "📝 Language Test Deadline: {month_year}",
        "lang_test_deadline_asap" : "📝 Language Test Deadline: ASAP",
        "vjo_renewal_warning": "⚠️ **Warning:** Your peak score is in >18 months. You will need to renew your VJO.",
        "calc_section_title": "### 📐 How is this calculated?",
        "calc_section_body": (
            "The simulation recalculates your official score for **every single square** in the grid. "
            "It assumes you continue working in your current role:\n\n"
            "$$\n"
            "\\text{Future Score} = \\text{Current Profile} + "
            "\\underbrace{\\text{Tenure Gain}}_{\\color{green}{\\text{Points } \\uparrow}} - "
            "\\underbrace{\\text{Age Decay}}_{\\color{red}{\\text{Points } \\downarrow}} + "
            "\\underbrace{\\text{Target French}}_{\\color{blue}{\\text{New Skill Level}}}\n"
            "$$"
        ),
        "calc_expander_title" : "ℹ️ See Calculation Details",
        "calc_section_expander" : (
            "1. **Starting Point:** We take your current profile (Age: **{age}**, Experience: **{exp}** months).\n"
            "2.  **Apply Time Travel:** For every month passed on the axis, we update:\n"
                "* ✅ **General & Quebec Experience:** You gain 1 month of experience.\n"
                "* ✅ **Shortage Job Tenure:** Your primary occupation tenure increases (re-calculating shortage points).\n"
                "* ✅ **Spouse Experience:** Your spouse gains 1 month of Quebec experience (if applicable).\n"
                "* ⚠️ **Age Decay (You & Spouse):** We calculate if you (or your spouse) cross a birthday threshold and deduct points accordingly.\n"
            "3.  **Apply Language Target:** We **replace** your current French test results with the level selected on the axis.\n"
        ),
        "target_score_label": "Target Score:",

        # Draws Tab
        "draws_title": "📢 Recent Invitation Rounds",
        "draws_sub": "Use these values to understand the cutoff scores for different streams.",
        "tip": "💡 **Tip:** Go to the 'Strategy Simulator' tab and select one of these rounds to visualize exactly what you need to do to reach the Green Zone.",
        "stream_def": "ℹ️ Stream Definitions",
        "total_invited": "Total invited (PSTQ Streams 1–4)",
        "stream1_label": "Stream 1 (Highly qualified and specialized skills)",
        "stream2_label": "Stream 2 (Intermediate and manual skills)",
        "stream3_label": "Stream 3 (Regulated professions)",
        "stream4_label": "Stream 4 (Exceptional talent)",
        "notes_stream1_diploma": "Québec diploma; FEER 0–2; non-regulated; Québec-wide",
        "notes_stream1_manufacturing": "Manufacturing & food processing; FEER 0–2; outside Montréal Metropolitan Community",
        "notes_stream2_priority": "Priority sectors (health & construction); FEER 3–5; Québec-wide",
        "notes_stream2_manufacturing": "Manufacturing & food processing; FEER 3–5; outside Montréal Metropolitan Community",
        "notes_stream3_priority": "Regulated professions; FEER 0–2; priority sectors; Québec residence",
        "notes_stream3_construction": "Regulated professions; FEER 3–5; construction & trades; Québec residence",
        "notes_stream1_std": "Standard Stream 1 selection",
        "notes_stream2_std": "Standard Stream 2 selection",
        "notes_stream3_std": "Standard Stream 3 selection",
        "notes_stream4_partner": "Partner positive opinion in targeted field OR exceptional achievement document; doctorate; 36 months experience in last 5 years",
        "notes_stream4_exceptional": "Exceptional achievement document; doctorate; 36 months experience in last 5 years",
        "notes_stream4_doctorate_equiv": "Partner positive opinion in targeted field OR exceptional achievement document; doctorate-equivalent; 36 months experience in last 5 years",
        "plan_2026_metric_label": "Estimated places remaining (Plan 2026 – Skilled workers)",
        "plan_2026_metric_help": (
            "Based on Québec’s 2026 immigration plan for skilled workers "
            "({min}–{max}). PSTQ selections made in 2025 are assumed to "
            "contribute primarily to 2026 admissions. This comparison is indicative."
        ),
        "plan_2026_caption": (
            "Current selections ≈ {pct_min}–{pct_max}% of the 2026 "
            "Skilled workers plan."
        ),

        "draws_table_caption": (
            "Each row is a published score cutoff within a draw. For Stream 4 "
            "(Exceptional talent), no score cutoff is published. “Invited” is the "
            "total invitations for that date and stream. The quota comparison is a "
            "forward-looking estimate against the 2026 skilled workers admission plan."
        ),

        "draws_ref_title": "References and sources",
        "draws_ref_body": (
            "- [Immigration Plan 2026 – MIFI (official PDF)]"
            "(https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/immigration/"
            "publications-adm/plan-immigration/PL_immigration_2026_MIFI.pdf)\n"
            "- [PSTQ Invitations in Arrima – Skilled Workers Selection Program (2025)]"
            "(https://www.quebec.ca/immigration/permanente/travailleurs-qualifies/"
            "programme-selection-travailleurs-qualifies/invitation/2025)"
        ),







        # --- TOOLTIPS (EXPLANATIONS) ---
        "tip_age": "Points are maximized between ages 18-30 and decrease progressively until age 45.",
        "tip_edu": "Points are awarded for your highest obtained diploma. (e.g., A Master's scores higher than a Bachelor's).",
        "tip_exp": "Full-time work experience (30h+/week) acquired in the last 5 years, anywhere in the world.",
        "tip_fr": "Points for Listening, Speaking, Reading, and Writing. NCLC Level 7 is the key threshold for higher points.",
        "tip_diag": "Bonus points if your primary occupation is listed as 'Deficit' (Shortage) in the government's annual planning.",
        "tip_qc_exp": "Work experience physically performed within the province of Quebec.",
        "tip_qc_dip": "Points if you obtained your diploma from a recognized Quebec educational institution.",
        "tip_vjo": "Requires a formal Validated Job Offer (VJO) approved by the Ministry (MIFI).",
        "tip_auth": "Points if you hold a license to practice for a regulated profession in Quebec (e.g., Nursing, Engineering).",
        "tip_reg": "Bonus points for living, working, or studying in regions outside the Montreal Metropolitan Area (CMM).",
        "tip_sp_gen": "Your spouse contributes points based on their Age, Education, French proficiency, and Quebec Experience.",

        # --- TEF/TEFAQ/TCF TRANSLATION TAB ---
        "tab4_title": "French Test Score Converter",
        "sel_test": "Step 1: Select your Test",
        # Context for TEF (Simple)
        "ctx_tef_title": "Understanding the TEF Scale",
        "ctx_tef_1": "• **Global Scale:** All 4 skills are scored out of **699**.",
        "ctx_tef_2": "• **Target:** Level 7 (B2) starts at **400 points**.",

        # Context for TCF (Complex)
        "ctx_tcf_title": "Understanding the TCF Scale (Hybrid)",
        "ctx_tcf_1": "• **Listening & Reading:** Scored out of **699**.",
        "ctx_tcf_2": "• **Speaking & Writing:** Scored out of **20**.",
        "ctx_tcf_warn": "⚠️ **Important:** Please ensure you enter your scores in the correct format below.",

        "enter_score": "Step 2: Enter your raw scores",
        "tab4_desc": "Convert your raw TEF/TEFAQ/TCF scores into the NCLC bands used for immigration points.",
        "sel_test": "Select Test Type",
        "enter_score": "Enter your raw scores below.",
        "tefaq_note": "TEFAQ focuses on Listening/Speaking. Enter 0 for others if not applicable.",
        "results_for": "Results: {test}",
        "col_skill": "Skill",
        "col_status": "Current Status",
        "col_dist": "Distance to Next Level",
        "max_reach": "Max Level 12 Reached! 🏆",
        "pts_need": "pts needed",
        "to_reach": "to reach Level",
        "start_lvl": "Start Lvl",
        "beginner": "Beginner",
        "context_header": "Understanding the Scale:",
        "context_1": "Max Score: 699 points.",
        "context_2": "Your Goal: Level 7 (B2) is usually the 'Golden Threshold' for Quebec.",
        "context_3": "The Bars: These show your progress *within your current level* towards the next one.",

        # References
        "ref_title": "### 📚 Official Scoring Grids (PSTQ)",
        "ref_intro": "This reference section details the exact point allocation used by the Ministry of Immigration (MIFI). Use these tables to verify your score calculation manually.",
        "ref_category_label": "Select Category to Explore:",
        "ref_cat1_label": "1. Human Capital (Age, Edu, French)",
        "ref_cat2_label": "2. Quebec Labor Needs (Work, VJO)",
        "ref_cat3_label": "3. Spouse & Adaptation",

        "ref_age_title": "📅 1. Age Points",
        "ref_age_caption": "Points are maximized from age 18 to 30, then decrease by ~5 points per year.",
        "ref_age_col_age": "Age",
        "ref_age_col_single": "Single Applicant",
        "ref_age_col_spouse": "With Spouse",

        "ref_edu_title": "🎓 2. Education Points",
        "ref_edu_caption": "Points based on the highest obtained diploma.",
        "ref_edu_col_level": "Diploma Level",
        "ref_edu_col_single": "Single",
        "ref_edu_col_spouse": "With Spouse",

        "ref_fr_title": "🗣️ 3. French Proficiency (Principal Applicant)",
        "ref_fr_caption": "Points are awarded per skill. **Level 7 (B2)** is the major threshold.",
        "ref_fr_col_nclc": "NCLC Level",
        "ref_fr_col_per_skill": "Points (per skill)",
        "ref_fr_col_single": "Points (Single)",
        "ref_fr_col_spouse": "Points (Spouse)",
        "ref_fr_row_1": "Level 1-4 (Beginner)",
        "ref_fr_row_2": "Level 5-6 (Low B1)",
        "ref_fr_row_3": "Level 7-8 (B2)",
        "ref_fr_row_4": "Level 9-12 (C1/C2)",
        "ref_fr_note": "**Note:** Total French Score = Sum of all 4 skills. Max possible is 200 (Single) or 160 (With Spouse).",

        "ref_qn_exp_title": "💼 1. Work Experience",
        "ref_qn_exp_caption": "Points are awarded based on cumulative full-time work experience in the last 5 years.",
        "ref_qn_exp_col_duration": "Duration",
        "ref_qn_exp_col_gen": "General Experience",
        "ref_qn_exp_col_gen_spouse": "Gen. Exp (With Spouse)",
        "ref_qn_exp_band_label": "{min} to {max} months",
        "ref_qn_exp_band_48plus": "48+ months",

        "ref_diag_title": "🏥 2. Job Shortage Diagnosis",
        "ref_diag_caption": "Bonus points if your occupation is on the Deficit list.",
        "ref_diag_col_diag": "Diagnosis",
        "ref_diag_col_points": "Points",
        "ref_diag_deficit": "Deficit (Déficitaire)",
        "ref_diag_slight": "Slight Deficit (Léger)",
        "ref_diag_balanced": "Balanced (Équilibré)",
        "ref_diag_deficit_points": "Max (Up to 120)",
        "ref_diag_slight_points": "Medium",
        "ref_diag_balanced_points": "0",

        "ref_qc_title": "⚜️ 3. Quebec Specifics",
        "ref_qc_diploma_title": "**Quebec Diploma (Criterium 5)**",
        "ref_qc_col_dip_type": "Diploma Type",
        "ref_qc_col_points": "Points",
        "ref_qc_other_title": "**Other Factors**",
        "ref_qc_col_factor": "Factor",
        "ref_qc_vjo_mtl": "Validated Job Offer (Montreal)",
        "ref_qc_vjo_outside": "Validated Job Offer (Outside MTL)",
        "ref_qc_reg_ties": "Regional Ties (Living >2 years)",
        "ref_qc_points_30": "30",
        "ref_qc_points_50": "50",
        "ref_qc_points_120": "Up to 120",

        "ref_sp_title": "❤️ Spouse / Common-Law Partner Factors",
        "ref_sp_intro": "If you apply with a spouse, the total score denominator changes. The spouse contributes points to the total.",

        "ref_sp_edu_title": "#### 1. Spouse Education",
        "ref_sp_edu_col_level": "Level",
        "ref_sp_edu_col_points": "Points",

        "ref_sp_age_title": "#### 2. Spouse Age",
        "ref_sp_age_col_age": "Age",
        "ref_sp_age_col_points": "Points",

        "ref_sp_fr_title": "#### 3. Spouse French (Oral Only)",
        "ref_sp_fr_caption": "Spouse points are usually awarded for Listening and Speaking only.",
        "ref_sp_fr_col_level": "Level",
        "ref_sp_fr_col_points": "Points",
        "ref_sp_fr_row_1": "Level 1-3",
        "ref_sp_fr_row_2": "Level 4",
        "ref_sp_fr_row_3": "Level 5-6",
        "ref_sp_fr_row_4": "Level 7-8",
        "ref_sp_fr_row_5": "Level 9+",

        "ref_sp_qc_title": "#### 4. Spouse Quebec Work",
        "ref_sp_qc_col_duration": "Duration",
        "ref_sp_qc_col_points": "Points",
        "ref_sp_qc_band_label": "{min} to {max} months",
        "ref_sp_qc_band_48plus": "48+ months",

        "ref_sources_title": "References and Sources",
        "ref_sources_pstq_link_label": "Official PSTQ Scoring Grid (MIFI)",

        # Contact
        "contact_title": "📬 Contact & Feedback",
    },

    "fr": {
        "app_title": "🍁 Simulateur PSTQ Québec",
        "app_subtitle": "Calculateur interactif pour le *Programme régulier des travailleurs qualifiés*.",
        "lang_select": "Langue / Language",

        # Sidebar
        "sb_title": "1. Configuration du Profil",
        "sec_applicant": "👤 Candidat (Vous)",
        "sec_job": "💼 Emploi et Liens Québec",
        "sec_spouse": "❤️ Conjoint(e)",
        "age": "Âge",
        "edu": "Éducation",
        "exp": "Expérience Totale (Mois)",
        "fr_skills": "Français (Échelle Québécoise Niveaux 1-12)",
        "list": "Compréhension Orale",
        "speak": "Production Orale",
        "read": "Compréhension Écrite",
        "write": "Production Écrite",

        "job_diag": "Diagnostic de l'emploi (Pénurie)",
        "job_prim_exp": "Exp. dans l'emploi en pénurie (Mois)",
        "job_qc_exp": "Expérience Travail Québec (Mois)",
        "vjo": "Offre d'emploi validée (OEV)",
        "auth": "Ordre Professionnel / Réglementé",
        "qc_dip": "Diplôme du Québec",
        "reg_ties": "Liens Régionaux (Hors Montréal)",
        "reg_res": "Mois de Résidence",
        "reg_work": "Mois de Travail",
        "reg_study": "Mois d'Études",

        "sp_check": "Accompagné par un conjoint",
        "sp_age": "Âge Conjoint",
        "sp_edu": "Édu Conjoint",
        "sp_qc_exp": "Exp. QC Conjoint (Mois)",
        "sp_fr": "Français Conjoint",
        "fam_check": "Famille au QC",

        # Tabs
        "tab_dash": "📊 Tableau de Bord",
        "tab_sim": "🚀 Simulateur",
        "tab_draws": "📜 Derniers Tirages",
        "tab_lang": "🌐 Convertisseur Français",
        "tab_job": "🕵️ Recherche d'Emploi",
        "tab_ref": "📚 Pointage Criteries",
        "tab_contact": "📬 Contact",

        # Job Search Tab
        "job_subheader": (
            "**Objectif :** Vérifier si votre profession est en **déficit** (fort potentiel de points).\n"
            "*Source de données : diagnostics gouvernementaux officiels*"
        ),
        "job_search_placeholder": "ex. Informatique, 21232",
        "job_filter_category": "Catégorie",
        "job_filter_diagnosis": "Diagnostic",

        "job_col_noc": "Code CNP",
        "job_col_title": "Titre d’emploi",
        "job_col_diag": "Diagnostic",
        "job_col_cat": "Catégorie",
        "job_stats_deficit": "Total des professions en déficit",
        "job_stats_deficit_delta": "Professions hautement prioritaires",
        "job_stats_slight_deficit" : "Total des professions en léger déficit",
        "job_stats_slight_deficit_delta": "Professions modérément prioritaires",
        "job_matches": "Affichage de **{n}** résultats :",
        "job_cat_chart_title": "Répartition des emplois par catégorie (filtre appliqué)",



        # Dashboard
        "hc": "Capital Humain",
        "qn": "Besoins du Québec",
        "ad": "Adaptabilité",
        "total_score": "SCORE TOTAL",
        "breakdown": "Voir le détail des points",
        "shortage": "Pénurie",

        # Simulator
        "sim_title": "🎯 Carte Stratégique",
        "sim_title_description": "Cet outil simule comment votre score évolue dans le temps. Crucial : Il prend en compte la perte de points liée à l'âge. En gagnant de l'expérience (points en hausse), vous vieillissez aussi (points en baisse).",
        "step1": "Étape 1: Définir votre Cible",
        "select_draw": "Choisir un tirage à battre:",
        "manual": "Entrée Manuelle",
        "step2": "Étape 2: Simuler le Futur",
        "x_axis": "Axe X (Bas)",
        "y_axis": "Axe Y (Gauche)",
        "green_zone": "Analyse Zone Verte (Seuil: {score})",
        "legend": "🟥 Rouge = Score sous le seuil | 🟩 Vert = Score ≥ seuil",
        "avg_cutoff": "Le score moyen de coupure est",
        "peq_tip": "💡 **Astuce :** Une cellule marquée d'une étoile ★ indique un point où le seuil simplifié de type PEQ (≥24 mois de travail au Québec + Français oral ≥7) serait atteint.",
        "strategy_timing": "### ⏳ Analyse Stratégique du Timing",
        "peq_met": "✅ Seuil PEQ atteint (programme historique)",
        "peq_not_met": "❌ Seuil PEQ non atteint",
        "peak_score": "📈 Votre score maximal : {score}",
        "peak_score_occurs" : "Cela se produit dans **{months} mois** ({date}).",
        "lang_test_deadline_label" : "📝 Date limite du test de langue : {month_year}",
        "lang_test_deadline_asap" : "📝 Date limite du test de langue : Dès que possible",
        "vjo_renewal_warning": "⚠️ **Attention :** Votre score maximal est dans plus de 18 mois. Vous devrez renouveler votre OEV.",
        "calc_section_title": "### 📐 Comment est-ce calculé ?",
        "calc_section_body": (
            "La simulation recalcule votre score officiel pour **chaque case** de la grille. "
            "Elle suppose que vous continuez à travailler dans votre poste actuel :\n\n"
            "$$\n"
            "\\text{Score futur} = \\text{Profil actuel} + "
            "\\underbrace{\\text{Gain d'ancienneté}}_{\\color{green}{\\text{Points } \\uparrow}} - "
            "\\underbrace{\\text{Perte liée à l'âge}}_{\\color{red}{\\text{Points } \\downarrow}} + "
            "\\underbrace{\\text{Français cible}}_{\\color{blue}{\\text{Nouveau niveau}}}\n"
            "$$"
        ),
        "calc_expander_title" : "ℹ️ Voir les détails du calcul",
        "calc_section_expander" : (
            "1. **Point de départ :** Nous utilisons votre profil actuel (Âge : **{age}**, Expérience : **{exp}** mois).\n"
            "2. **Application du “Time Travel” :** Pour chaque mois ajouté sur l’axe, nous mettons à jour :\n"
                "* ✅ **Expérience générale et au Québec :** vous gagnez 1 mois d’expérience.\n"
                "* ✅ **Ancienneté en emploi en pénurie :** votre ancienneté dans l’occupation principale augmente (recalcul des points de pénurie).\n"
                "* ✅ **Expérience du conjoint :** votre conjoint gagne 1 mois d’expérience au Québec (le cas échéant).\n"
                "* ⚠️ **Impact de l’âge (vous & conjoint) :** nous vérifions si vous (ou votre conjoint) franchissez un seuil d’âge et ajustons les points.\n"
            "3.  **Application du français cible :** nous **remplaçons** vos résultats actuels en français par le niveau sélectionné sur l’axe.\n"
        ),
        "target_score_label": "Score Cible :",



        # Draws Tab
        "draws_title": "📢 Rondes d'invitation récentes",
        "draws_sub": "Utilisez ces valeurs pour comprendre les scores de coupure.",
        "tip": "💡 **Astuce:** Allez dans l'onglet 'Simulateur' et sélectionnez une de ces rondes pour visualiser comment atteindre la Zone Verte.",
        "stream_def": "ℹ️ Définitions des Volets",
        "total_invited": "Total des invités (Volet PSTQ 1 à 4)",
        "average_cutoff": "Score moyen requis (filières 1 à 3)",
        "stream1_label": "Volet 1 : Haute qualification et compétences spécialisées",
        "stream2_label": "Volet 2 : Compétences intermédiaires et manuelles",
        "stream3_label": "Volet 3 : Professions réglementées",
        "stream4_label": "Volet 4 : Talents d’exception",
        "notes_stream1_diploma": "Diplôme du Québec; FEER 0–2; non réglementé; partout au Québec",
        "notes_stream1_manufacturing": "Fabrication & transformation alimentaire; FEER 0–2; hors Communauté métropolitaine de Montréal",
        "notes_stream2_priority": "Secteurs prioritaires (santé & construction); FEER 3–5; partout au Québec",
        "notes_stream2_manufacturing": "Fabrication & transformation alimentaire; FEER 3–5; hors Communauté métropolitaine de Montréal",
        "notes_stream3_priority": "Professions réglementées; FEER 0–2; secteurs prioritaires; résidence au Québec",
        "notes_stream3_construction": "Professions réglementées; FEER 3–5; construction & métiers; résidence au Québec",
        "notes_stream1_std": "Sélection standard Volet 1",
        "notes_stream2_std": "Sélection standard Volet 2",
        "notes_stream3_std": "Sélection standard Volet 3",
        "notes_stream4_partner": "Avis positif d’un partenaire dans un domaine ciblé OU document d’accomplissement exceptionnel; doctorat; 36 mois d’expérience dans les 5 dernières années",
        "notes_stream4_exceptional": "Document d’accomplissement exceptionnel; doctorat; 36 mois d’expérience dans les 5 dernières années",
        "notes_stream4_doctorate_equiv": "Avis positif d’un partenaire dans un domaine ciblé OU document d’accomplissement exceptionnel; équivalent doctorat; 36 mois d’expérience dans les 5 dernières années",
        "plan_2026_metric_label": "Places estimées restantes (Plan 2026 – Travailleurs qualifiés)",
        "plan_2026_metric_help": (
            "Basé sur le Plan d’immigration 2026 du Québec pour les travailleurs qualifiés "
            "({min}–{max}). Les sélections PSTQ effectuées en 2025 sont supposées contribuer "
            "principalement aux admissions de 2026. Cette comparaison est indicative."
        ),
        "plan_2026_caption": (
            "Sélections actuelles ≈ {pct_min}–{pct_max}% du plan 2026 "
            "des travailleurs qualifiés."
        ),

        "draws_table_caption": (
            "Chaque ligne correspond à un seuil de score publié pour un tirage. Pour le Volet 4 "
            "(Talents d’exception), aucun seuil de score n’est publié. « Invitée(s) » indique le "
            "nombre total d’invitations pour cette date et ce volet. La comparaison au quota est "
            "une estimation projetée par rapport au plan d’admissions 2026 des travailleurs qualifiés."
        ),

        "draws_ref_title": "Références et sources",
        "draws_ref_body": (
            "- [Plan d’immigration 2026 – MIFI (PDF officiel)]"
            "(https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/immigration/"
            "publications-adm/plan-immigration/PL_immigration_2026_MIFI.pdf)\n"
            "- [Invitations dans Arrima du Programme de sélection des travailleurs qualifiés (2025)]"
            "(https://www.quebec.ca/immigration/permanente/travailleurs-qualifies/"
            "programme-selection-travailleurs-qualifies/invitation/2025)"
        ),


        # --- TOOLTIPS (EXPLANATIONS) ---
        "tip_age": "Les points sont maximisés entre 18 et 30 ans et diminuent progressivement jusqu'à 45 ans.",
        "tip_edu": "Points attribués pour votre diplôme le plus élevé (ex: Maîtrise vaut plus que Baccalauréat).",
        "tip_exp": "Expérience de travail à temps plein (30h+/sem) acquise au cours des 5 dernières années, n'importe où dans le monde.",
        "tip_fr": "Points pour Écoute, Parler, Lecture, Écriture. Le niveau NCLC 7 est le seuil clé.",
        "tip_diag": "Points bonus si votre profession est listée comme 'Déficitaire' (Pénurie) dans la planification annuelle.",
        "tip_qc_exp": "Expérience de travail effectuée physiquement sur le territoire québécois.",
        "tip_qc_dip": "Points si vous avez obtenu votre diplôme dans un établissement d'enseignement du Québec.",
        "tip_vjo": "Nécessite une Offre d'emploi validée (OEV) formellement approuvée par le MIFI.",
        "tip_auth": "Points si vous détenez un permis d'exercice pour une profession réglementée (ex: Ordre des ingénieurs).",
        "tip_reg": "Points bonus pour vivre, travailler ou étudier dans une région hors de la Communauté métropolitaine de Montréal (CMM).",
        "tip_sp_gen": "Votre conjoint(e) contribue des points selon son Âge, sa Scolarité, son Français et son Expérience au Québec.",

        # --- TEF/TEFAQ/TCF TRANSLATION TAB ---
        "tab4_title": "Convertisseur de scores",
        "sel_test": "Étape 1 : Choisissez votre test",
        # Context for TEF
        "ctx_tef_title": "Comprendre l'échelle TEF",
        "ctx_tef_1": "• **Échelle Globale :** Les 4 compétences sont notées sur **699**.",
        "ctx_tef_2": "• **Cible :** Le Niveau 7 (B2) commence à **400 points**.",

        # Context for TCF
        "ctx_tcf_title": "Comprendre l'échelle TCF (Hybride)",
        "ctx_tcf_1": "• **Écoute et Lecture :** Notés sur **699**.",
        "ctx_tcf_2": "• **Parler et Écrire :** Notés sur **20**.",
        "ctx_tcf_warn": "⚠️ **Important :** Assurez-vous d'entrer vos scores dans le bon format ci-dessous.",

        "enter_score": "Étape 2 : Entrez vos scores",
        "tab4_desc": "Convertissez vos scores bruts TEF/TEFAQ/TCF en niveaux NCLC.",
        "sel_test": "Choisir le test",
        "enter_score": "Entrez vos scores bruts ci-dessous.",
        "tefaq_note": "Le TEFAQ cible l'Écoute/Parler. Entrez 0 pour les autres si non applicable.",
        "results_for": "Résultats : {test}",
        "col_skill": "Compétence",
        "col_status": "Statut Actuel",
        "col_dist": "Distance au prochain niveau",
        "max_reach": "Niveau Max 12 Atteint! 🏆",
        "pts_need": "pts requis",
        "to_reach": "pour atteindre le Niveau",
        "start_lvl": "Début Niv",
        "beginner": "Débutant",
        "context_header": "Comprendre l'échelle :",
        "context_1": "Score Max : 699 points.",
        "context_2": "Votre But : Le Niveau 7 (B2) est souvent le seuil clé pour le Québec.",
        "context_3": "Les Barres : Elles montrent votre progression *au sein de votre niveau actuel* vers le suivant.",

        # References
        "ref_title": "### 📚 Grilles officielles de pointage (PSTQ)",
        "ref_intro": "Cette section de référence présente en détail l’attribution exacte des points utilisée par le ministère de l’Immigration (MIFI). Utilisez ces tableaux pour vérifier manuellement le calcul de votre score.",
        "ref_category_label": "Sélectionnez la catégorie à explorer :",
        "ref_cat1_label": "1. Capital humain (Âge, Études, Français)",
        "ref_cat2_label": "2. Besoins du marché du travail au Québec (Emploi, OVV)",
        "ref_cat3_label": "3. Conjoint(e) & adaptation",

        "ref_age_title": "📅 1. Points liés à l’âge",
        "ref_age_caption": "Les points sont maximisés entre 18 et 30 ans, puis diminuent d’environ 5 points par année.",
        "ref_age_col_age": "Âge",
        "ref_age_col_single": "Demandeur seul",
        "ref_age_col_spouse": "Avec conjoint(e)",

        "ref_edu_title": "🎓 2. Points liés à la scolarité",
        "ref_edu_caption": "Points attribués selon le diplôme le plus élevé obtenu.",
        "ref_edu_col_level": "Niveau de diplôme",
        "ref_edu_col_single": "Sans conjoint(e)",
        "ref_edu_col_spouse": "Avec conjoint(e)",

        "ref_fr_title": "🗣️ 3. Compétences en français (requérant principal)",
        "ref_fr_caption": "Les points sont accordés par compétence. **Le niveau 7 (B2)** constitue le seuil clé.",
        "ref_fr_col_nclc": "Niveau NCLC",
        "ref_fr_col_per_skill": "Points (par compétence)",
        "ref_fr_col_single": "Points (sans conjoint)",
        "ref_fr_col_spouse": "Points (avec conjoint)",
        "ref_fr_row_1": "Niveaux 1–4 (débutant)",
        "ref_fr_row_2": "Niveaux 5–6 (B1 faible)",
        "ref_fr_row_3": "Niveaux 7–8 (B2)",
        "ref_fr_row_4": "Niveaux 9–12 (C1/C2)",
        "ref_fr_note": "**Note :** Le score total en français correspond à la somme des 4 compétences. Le maximum possible est de 200 points (sans conjoint) ou 160 points (avec conjoint).",

        "ref_qn_exp_title": "💼 1. Expérience de travail",
        "ref_qn_exp_caption": "Les points sont accordés selon l’expérience de travail à temps plein cumulée au cours des 5 dernières années.",
        "ref_qn_exp_col_duration": "Durée",
        "ref_qn_exp_col_gen": "Expérience générale",
        "ref_qn_exp_col_gen_spouse": "Exp. gén. (avec conjoint)",
        "ref_qn_exp_band_label": "{min} à {max} mois",
        "ref_qn_exp_band_48plus": "48 mois et plus",

        "ref_diag_title": "🏥 2. Diagnostic de pénurie de main-d’œuvre",
        "ref_diag_caption": "Des points boni sont accordés si votre profession figure sur la liste des professions en déficit.",
        "ref_diag_col_diag": "Diagnostic",
        "ref_diag_col_points": "Points",
        "ref_diag_deficit": "Déficitaire",
        "ref_diag_slight": "Légèrement déficitaire",
        "ref_diag_balanced": "Équilibrée",
        "ref_diag_deficit_points": "Maximum (jusqu’à 120)",
        "ref_diag_slight_points": "Intermédiaire",
        "ref_diag_balanced_points": "0",

        "ref_qc_title": "⚜️ 3. Spécificités québécoises",
        "ref_qc_diploma_title": "**Diplôme du Québec (critère 5)**",
        "ref_qc_col_dip_type": "Type de diplôme",
        "ref_qc_col_points": "Points",
        "ref_qc_other_title": "**Autres facteurs**",
        "ref_qc_col_factor": "Facteur",
        "ref_qc_vjo_mtl": "Offre d’emploi validée (Montréal)",
        "ref_qc_vjo_outside": "Offre d’emploi validée (hors Montréal)",
        "ref_qc_reg_ties": "Liens régionaux (résidence > 2 ans)",
        "ref_qc_points_30": "30",
        "ref_qc_points_50": "50",
        "ref_qc_points_120": "Jusqu’à 120",

        "ref_sp_title": "❤️ Facteurs liés au conjoint ou conjoint de fait",
        "ref_sp_intro": "Si vous présentez votre demande avec un(e) conjoint(e), le dénominateur total du score change. Le ou la conjoint(e) contribue au score global.",

        "ref_sp_edu_title": "#### 1. Scolarité du conjoint",
        "ref_sp_edu_col_level": "Niveau",
        "ref_sp_edu_col_points": "Points",

        "ref_sp_age_title": "#### 2. Âge du conjoint",
        "ref_sp_age_col_age": "Âge",
        "ref_sp_age_col_points": "Points",

        "ref_sp_fr_title": "#### 3. Français du conjoint (oral seulement)",
        "ref_sp_fr_caption": "Les points du conjoint sont généralement attribués uniquement pour la compréhension et l’expression orales.",
        "ref_sp_fr_col_level": "Niveau",
        "ref_sp_fr_col_points": "Points",
        "ref_sp_fr_row_1": "Niveaux 1–3",
        "ref_sp_fr_row_2": "Niveau 4",
        "ref_sp_fr_row_3": "Niveaux 5–6",
        "ref_sp_fr_row_4": "Niveaux 7–8",
        "ref_sp_fr_row_5": "Niveau 9 et plus",

        "ref_sp_qc_title": "#### 4. Expérience de travail du conjoint au Québec",
        "ref_sp_qc_col_duration": "Durée",
        "ref_sp_qc_col_points": "Points",
        "ref_sp_qc_band_label": "{min} à {max} mois",
        "ref_sp_qc_band_48plus": "48 mois et plus",

        "ref_sources_title": "Références et sources",
        "ref_sources_pstq_link_label": "Grille officielle de pointage du PSTQ (MIFI)",

        # Contact
        "contact_title": "📬 Contact et commentaires",

    }
}
