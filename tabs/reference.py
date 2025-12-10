# tabs/reference.py
import streamlit as st
import pandas as pd
import translations as tr
import logic.scoring as scoring

def render(t, scoring, tr):
    """
    Renders the Official Scoring Reference tab.
    Args:
        t: Translation function
        scoring: The logic.scoring module (access to constants)
        tr: The translations module (access to maps)
    """
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
                "Single Applicant": scoring.AGE_SINGLE.get(age, 0),
                "With Spouse": scoring.AGE_SPOUSE_PA.get(age, 0)
            })
        st.dataframe(pd.DataFrame(age_data), hide_index=True, width='stretch')

        st.divider()

        # 2. EDUCATION SECTION
        st.subheader("🎓 2. Education Points")
        st.caption("Points based on the highest obtained diploma.")

        edu_data = []
        # Use the constants from scoring.py
        for key, val in scoring.EDU_POINTS_UI.items():
            edu_data.append({
                "Diploma Level": tr.EDU_MAP.get(key, {}).get(st.session_state.lang, key),
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
        for band in scoring.EXP_PA_SINGLE:
            label = f"{band[0]} to {band[1]-1} months"
            if band[1] > 1000: label = "48+ months"

            sp_val = 0
            for sb in scoring.EXP_PA_SPOUSE:
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

        st.markdown("**Quebec Diploma (Criterium 5)**")
        qc_dip_data = [{"Diploma Type": k, "Points": v} for k,v in scoring.QC_DIPLOMA_POINTS.items()]
        st.dataframe(pd.DataFrame(qc_dip_data), hide_index=True, width='stretch')

        st.markdown("**Other Factors**")
        qc_data = [
            {"Factor": "Validated Job Offer (Montreal)", "Points": "30"},
            {"Factor": "Validated Job Offer (Outside MTL)", "Points": "50"},
            {"Factor": "Regional Ties (Living >2 years)", "Points": "Up to 120"},
        ]
        st.dataframe(pd.DataFrame(qc_data), hide_index=True, width='stretch')

    # --- CATEGORY 3: SPOUSE ---
    elif "3." in grid_cat:
        st.subheader("❤️ Spouse / Common-Law Partner Factors")
        st.markdown("If you apply with a spouse, the total score denominator changes. The spouse contributes points to the total.")

        st.divider()

        st.markdown("#### 1. Spouse Education")
        sp_edu_data = [{"Level": k, "Points": v} for k, v in scoring.EDU_SPOUSE_UI.items()]
        st.dataframe(pd.DataFrame(sp_edu_data), hide_index=True, width='stretch')

        st.divider()

        st.markdown("#### 2. Spouse Age")
        sp_age_data = [{"Age": str(k), "Points": v} for k, v in scoring.SP_AGE_ADAPT.items() if k % 2 == 0]
        st.dataframe(pd.DataFrame(sp_age_data), hide_index=True, width='stretch')

        st.divider()

        st.markdown("#### 3. Spouse French (Oral Only)")
        st.caption("Spouse points are usually awarded for Listening and Speaking only.")
        sp_fr_data = [
            {"Level": "Level 1-3", "Points": "0"},
            {"Level": "Level 4", "Points": "4"},
            {"Level": "Level 5-6", "Points": "6"},
            {"Level": "Level 7-8", "Points": "8"},
            {"Level": "Level 9+", "Points": "10"},
        ]
        st.table(pd.DataFrame(sp_fr_data))

        st.divider()

        st.markdown("#### 4. Spouse Quebec Work")
        sp_qc_data = []
        for band in scoring.SP_QC_EXP_TABLE:
            label = f"{band[0]} to {band[1]-1} months"
            if band[1] > 1000: label = "48+ months"
            sp_qc_data.append({"Duration": label, "Points": band[2]})
        st.dataframe(pd.DataFrame(sp_qc_data), hide_index=True, width='stretch')

    # --- References ---
    st.divider()
    st.subheader("References and Sources")
    st.markdown("""
    - [Official PSTQ Scoring Grid (MIFI)](https://cdn-contenu.quebec.ca/cdn-contenu/immigration/publications/fr/Pointage_criteres.pdf)
    """)
