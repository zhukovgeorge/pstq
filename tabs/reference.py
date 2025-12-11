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
    st.markdown(t("ref_title"))
    st.markdown(t("ref_intro"))

    grid_cat = st.radio(
        t("ref_category_label"),
        [t("ref_cat1_label"), t("ref_cat2_label"), t("ref_cat3_label")],
        horizontal=True
    )

    st.divider()

    # --- CATEGORY 1: HUMAN CAPITAL ---
    if "1." in grid_cat:
        # 1. AGE SECTION
        st.subheader(t("ref_age_title"))
        st.caption(t("ref_age_caption"))

        age_data = []
        for age in range(18, 46):
            age_data.append({
                t("ref_age_col_age"): str(age) if age < 45 else "45+",
                t("ref_age_col_single"): scoring.AGE_SINGLE.get(age, 0),
                t("ref_age_col_spouse"): scoring.AGE_SPOUSE_PA.get(age, 0),
            })
        st.dataframe(pd.DataFrame(age_data), hide_index=True, width='stretch')

        st.divider()

        # 2. EDUCATION SECTION
        st.subheader(t("ref_edu_title"))
        st.caption(t("ref_edu_caption"))

        edu_data = []
        # Use the constants from scoring.py
        for key, val in scoring.EDU_POINTS_UI.items():
            edu_data.append({
                t("ref_edu_col_level"): tr.EDU_MAP.get(key, {}).get(st.session_state.lang, key),
                t("ref_edu_col_single"): val[0],
                t("ref_edu_col_spouse"): val[1],
            })
        st.dataframe(pd.DataFrame(edu_data), hide_index=True, width='stretch')

        st.divider()

        # 3. FRENCH SECTION
        st.subheader(t("ref_fr_title"))
        st.caption(t("ref_fr_caption"))

        fr_data = [
            {
                t("ref_fr_col_nclc"): t("ref_fr_row_1"),
                t("ref_fr_col_per_skill"): "0",
            },
            {
                t("ref_fr_col_nclc"): t("ref_fr_row_2"),
                t("ref_fr_col_single"): "38",
                t("ref_fr_col_spouse"): "30",
            },
            {
                t("ref_fr_col_nclc"): t("ref_fr_row_3"),
                t("ref_fr_col_single"): "44",
                t("ref_fr_col_spouse"): "35",
            },
            {
                t("ref_fr_col_nclc"): t("ref_fr_row_4"),
                t("ref_fr_col_single"): "50",
                t("ref_fr_col_spouse"): "40",
            },
        ]
        st.table(pd.DataFrame(fr_data))
        st.info(t("ref_fr_note"))

    # --- CATEGORY 2: QUEBEC NEEDS ---
    elif "2." in grid_cat:
        # 1. WORK EXPERIENCE
        st.subheader(t("ref_qn_exp_title"))
        st.caption(t("ref_qn_exp_caption"))

        exp_data = []
        for band in scoring.EXP_PA_SINGLE:
            label = t("ref_qn_exp_band_label").format(min=band[0], max=band[1] - 1)
            if band[1] > 1000:
                label = t("ref_qn_exp_band_48plus")

            sp_val = 0
            for sb in scoring.EXP_PA_SPOUSE:
                if sb[0] == band[0]:
                    sp_val = sb[2]

            exp_data.append({
                t("ref_qn_exp_col_duration"): label,
                t("ref_qn_exp_col_gen"): band[2],
                t("ref_qn_exp_col_gen_spouse"): sp_val,
            })
        st.dataframe(pd.DataFrame(exp_data), hide_index=True, width='stretch')

        st.divider()

        # 2. JOB SHORTAGE
        st.subheader(t("ref_diag_title"))
        st.caption(t("ref_diag_caption"))
        diag_data = [
            {
                t("ref_diag_col_diag"): t("ref_diag_deficit"),
                t("ref_diag_col_points"): t("ref_diag_deficit_points"),
            },
            {
                t("ref_diag_col_diag"): t("ref_diag_slight"),
                t("ref_diag_col_points"): t("ref_diag_slight_points"),
            },
            {
                t("ref_diag_col_diag"): t("ref_diag_balanced"),
                t("ref_diag_col_points"): t("ref_diag_balanced_points"),
            },
        ]
        st.table(pd.DataFrame(diag_data))

        st.divider()

        # 3. QUEBEC SPECIFICS
        st.subheader(t("ref_qc_title"))

        st.markdown(t("ref_qc_diploma_title"))
        qc_dip_data = [
            {
                t("ref_qc_col_dip_type"): k,
                t("ref_qc_col_points"): v,
            }
            for k, v in scoring.QC_DIPLOMA_POINTS.items()
        ]
        st.dataframe(pd.DataFrame(qc_dip_data), hide_index=True, width='stretch')

        st.markdown(t("ref_qc_other_title"))
        qc_data = [
            {
                t("ref_qc_col_factor"): t("ref_qc_vjo_mtl"),
                t("ref_qc_col_points"): t("ref_qc_points_30"),
            },
            {
                t("ref_qc_col_factor"): t("ref_qc_vjo_outside"),
                t("ref_qc_col_points"): t("ref_qc_points_50"),
            },
            {
                t("ref_qc_col_factor"): t("ref_qc_reg_ties"),
                t("ref_qc_col_points"): t("ref_qc_points_120"),
            },
        ]
        st.dataframe(pd.DataFrame(qc_data), hide_index=True, width='stretch')

    # --- CATEGORY 3: SPOUSE ---
    elif "3." in grid_cat:
        st.subheader(t("ref_sp_title"))
        st.markdown(t("ref_sp_intro"))

        st.divider()

        st.markdown(t("ref_sp_edu_title"))
        sp_edu_data = [
            {
                t("ref_sp_edu_col_level"): k,
                t("ref_sp_edu_col_points"): v,
            }
            for k, v in scoring.EDU_SPOUSE_UI.items()
        ]
        st.dataframe(pd.DataFrame(sp_edu_data), hide_index=True, width='stretch')

        st.divider()

        st.markdown(t("ref_sp_age_title"))
        sp_age_data = [
            {
                t("ref_sp_age_col_age"): str(k),
                t("ref_sp_age_col_points"): v,
            }
            for k, v in scoring.SP_AGE_ADAPT.items()
            if k % 2 == 0
        ]
        st.dataframe(pd.DataFrame(sp_age_data), hide_index=True, width='stretch')

        st.divider()

        st.markdown(t("ref_sp_fr_title"))
        st.caption(t("ref_sp_fr_caption"))
        sp_fr_data = [
            {
                t("ref_sp_fr_col_level"): t("ref_sp_fr_row_1"),
                t("ref_sp_fr_col_points"): "0",
            },
            {
                t("ref_sp_fr_col_level"): t("ref_sp_fr_row_2"),
                t("ref_sp_fr_col_points"): "4",
            },
            {
                t("ref_sp_fr_col_level"): t("ref_sp_fr_row_3"),
                t("ref_sp_fr_col_points"): "6",
            },
            {
                t("ref_sp_fr_col_level"): t("ref_sp_fr_row_4"),
                t("ref_sp_fr_col_points"): "8",
            },
            {
                t("ref_sp_fr_col_level"): t("ref_sp_fr_row_5"),
                t("ref_sp_fr_col_points"): "10",
            },
        ]
        st.table(pd.DataFrame(sp_fr_data))

        st.divider()

        st.markdown(t("ref_sp_qc_title"))
        sp_qc_data = []
        for band in scoring.SP_QC_EXP_TABLE:
            label = t("ref_sp_qc_band_label").format(min=band[0], max=band[1] - 1)
            if band[1] > 1000:
                label = t("ref_sp_qc_band_48plus")
            sp_qc_data.append({
                t("ref_sp_qc_col_duration"): label,
                t("ref_sp_qc_col_points"): band[2],
            })
        st.dataframe(pd.DataFrame(sp_qc_data), hide_index=True, width='stretch')

    # --- References ---
    st.divider()
    st.subheader(t("ref_sources_title"))
    st.markdown(
        f"- [{t('ref_sources_pstq_link_label')}]"
        "(https://cdn-contenu.quebec.ca/cdn-contenu/immigration/publications/fr/Pointage_criteres.pdf)"
    )
