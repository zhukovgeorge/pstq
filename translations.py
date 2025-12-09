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
        "lang_select": "Langue / ",

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
        "step1": "Step 1: Set your Target",
        "select_draw": "Select a Draw Round to Beat:",
        "manual": "Manual Entry",
        "step2": "Step 2: Simulate Future Scenarios",
        "x_axis": "X-Axis (Bottom)",
        "y_axis": "Y-Axis (Left)",
        "green_zone": "Green Zone Analysis (Cutoff: {score})",
        "legend": "🟥 Red = Below Target | 🟩 Green = Qualified for Invitation",

        # Draws Tab
        "draws_title": "📢 Recent Invitation Rounds",
        "draws_sub": "Use these values to understand the cutoff scores for different streams.",
        "tip": "💡 **Tip:** Go to the 'Strategy Simulator' tab and select one of these rounds to visualize exactly what you need to do to reach the Green Zone.",
        "stream_def": "ℹ️ Stream Definitions",

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
        "tab_ref": "📚 Grilles Officielles",
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
        "step1": "Étape 1: Définir votre Cible",
        "select_draw": "Choisir un tirage à battre:",
        "manual": "Entrée Manuelle",
        "step2": "Étape 2: Simuler le Futur",
        "x_axis": "Axe X (Bas)",
        "y_axis": "Axe Y (Gauche)",
        "green_zone": "Analyse Zone Verte (Seuil: {score})",
        "legend": "🟥 Rouge = Sous la cible | 🟩 Vert = Qualifié pour invitation",

        # Draws Tab
        "draws_title": "📢 Rondes d'invitation récentes",
        "draws_sub": "Utilisez ces valeurs pour comprendre les scores de coupure.",
        "tip": "💡 **Astuce:** Allez dans l'onglet 'Simulateur' et sélectionnez une de ces rondes pour visualiser comment atteindre la Zone Verte.",
        "stream_def": "ℹ️ Définitions des Volets",

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
    }
}
