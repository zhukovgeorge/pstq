# translations.py

# ==========================================
# 1. MAPPINGS FOR LOGIC-HEAVY INPUTS
# ==========================================

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

# ==========================================
# 2. GENERAL UI TEXT
# ==========================================

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
    }
}
