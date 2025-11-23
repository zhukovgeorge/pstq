# translations.py

# 1. MAPPINGS FOR LOGIC-HEAVY INPUTS
# Keys = The English values your scoring engine expects
# Values = The Display text (EN / FR)

EDU_MAP = {
    "PhD": {"en": "PhD", "fr": "Doctorat"},
    "Masters": {"en": "Masters", "fr": "Maîtrise"},
    "Bachelors 3y+": {"en": "Bachelors 3y+", "fr": "Baccalauréat 3 ans+"},
    "Bachelors 2y": {"en": "Bachelors 2y", "fr": "Baccalauréat 2 ans"},
    "Tech Diploma 3y": {"en": "Tech Diploma 3y", "fr": "DEC Technique / Diplôme 3 ans"},
    "High School": {"en": "High School", "fr": "Secondaire (DES)"}
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
    "None": {"en": "None", "fr": "Aucun"},
    "PhD": {"en": "PhD", "fr": "Doctorat"},
    "Masters": {"en": "Masters", "fr": "Maîtrise"},
    "Bachelors 3y+": {"en": "Bachelors 3y+", "fr": "Baccalauréat 3 ans+"},
    "Bachelors 2y": {"en": "Bachelors 2y", "fr": "Baccalauréat 2 ans"},
    "Tech Diploma 3y": {"en": "Tech Diploma 3y", "fr": "DEC Technique / Diplôme 3 ans"},
    "Vocational (DEP)": {"en": "Vocational (DEP)", "fr": "DEP (1800h)"}
}

AXIS_MAP_LABELS = {
    "time_travel": {"en": "Future Months Worked", "fr": "Mois Travaillés (Futur)"},
    "fr_target": {"en": "My French Target (All Skills)", "fr": "Cible Français (Moi)"},
    "sp_fr_target": {"en": "Spouse French Target (All Skills)", "fr": "Cible Français (Conjoint)"}
}

# 2. GENERAL UI TEXT
TEXTS = {
    "en": {
        "app_title": "🍁 Quebec PSTQ Simulator",
        "app_subtitle": "Interactive score calculator for the *Regular Skilled Worker Program*.",
        "lang_select": "Language / Langue",

        # Sidebar
        "sb_title": "1. Profile Setup",
        "sec_applicant": "👤 Applicant (You)",
        "sec_job": "💼 Job & Quebec Ties",
        "sec_spouse": "❤️ Spouse / Partner",
        "age": "Age",
        "edu": "Education",
        "exp": "Total Career Exp (Months)",
        "fr_skills": "French Skills (Level 1-12)",
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

        # Dashboard
        "hc": "Human Capital",
        "qn": "Quebec Needs",
        "ad": "Adaptation",
        "total_score": "TOTAL SCORE",
        "passing_bench": "(General Passing Benchmark ~590+)",
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
        "stream_def": "ℹ️ Stream Definitions"
    },

    "fr": {
        "app_title": "🍁 Simulateur PSTQ Québec",
        "app_subtitle": "Calculateur interactif pour le *Programme régulier des travailleurs qualifiés*.",
        "lang_select": "Language / Langue",

        # Sidebar
        "sb_title": "1. Configuration du Profil",
        "sec_applicant": "👤 Candidat (Vous)",
        "sec_job": "💼 Emploi et Liens Québec",
        "sec_spouse": "❤️ Conjoint(e)",
        "age": "Âge",
        "edu": "Éducation",
        "exp": "Expérience Totale (Mois)",
        "fr_skills": "Compétences Français (Niveau 1-12)",
        "list": "Écoute",
        "speak": "Parler",
        "read": "Lecture",
        "write": "Écriture",

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

        # Dashboard
        "hc": "Capital Humain",
        "qn": "Besoins du Québec",
        "ad": "Adaptabilité",
        "total_score": "SCORE TOTAL",
        "passing_bench": "(Seuil de passage général ~590+)",
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
        "stream_def": "ℹ️ Définitions des Volets"
    }
}
