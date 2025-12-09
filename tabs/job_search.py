# tabs/job_search.py
import streamlit as st
import pandas as pd
import plotly.express as px
import job_data
import translations as tr


def _value_label(map_dict, raw_value: str) -> str:
    """Return localized label for a raw value."""
    lang = st.session_state.lang
    return map_dict.get(raw_value, {}).get(lang, raw_value)


def _label_to_raw(map_dict, label: str) -> str:
    """Map a localized label back to its raw value."""
    lang = st.session_state.lang
    for raw, langs in map_dict.items():
        if langs.get(lang) == label:
            return raw
    # Fallback: assume it's already raw
    return label


def render(t):
    # --- HEADER ---
    st.header(t("tab_job"))
    st.markdown(t("job_subheader"))

    # --- 1. LOAD DATA ---
    df_jobs = pd.DataFrame(job_data.JOBS)

    # Decide which source title column to use based on language
    lang = st.session_state.lang
    source_title_col = "Title (FR)" if lang == "fr" else "Title (EN)"

    df_jobs = df_jobs.copy()
    df_jobs["Title"] = df_jobs[source_title_col]

    # Optionally drop language-specific title columns so they don't appear
    for col in ["Title (FR)", "Title (EN)"]:
        if col in df_jobs.columns:
            df_jobs.drop(columns=col, inplace=True)

    # --- 2. DASHBOARD STATS (raw diagnosis) ---
    deficit_count = len(df_jobs[df_jobs["Diagnosis"].str.contains("Déficit", na=False)])
    st.metric(
        t("job_stats_deficit"),
        deficit_count,
        delta=t("job_stats_deficit_delta"),
    )

    st.divider()

    # --- 3. SEARCH & FILTERS ---
    col_search, col_cat, col_diag = st.columns([2, 1, 1])

    search_txt = col_search.text_input(
        "🔍 " + t("tab_job"),
        placeholder=t("job_search_placeholder"),
    )

    # CATEGORY FILTER (localized options)
    cat_raw_vals = sorted(df_jobs["Category"].dropna().unique().tolist())
    cat_display_vals = [_value_label(tr.JOB_CAT_VALUE_MAP, v) for v in cat_raw_vals]
    cat_opts = ["All"] + cat_display_vals
    sel_cat_label = col_cat.selectbox(t("job_filter_category"), cat_opts)

    # DIAGNOSTIC FILTER (localized options)
    diag_raw_vals = sorted(df_jobs["Diagnosis"].dropna().unique().tolist())
    diag_display_vals = [_value_label(tr.JOB_DIAG_VALUE_MAP, v) for v in diag_raw_vals]
    diag_opts = ["All"] + diag_display_vals
    sel_diag_label = col_diag.selectbox(t("job_filter_diagnosis"), diag_opts)

    # Apply Filters with RAW values
    filtered = df_jobs.copy()

    if search_txt:
        mask = filtered.astype(str).apply(
            lambda x: x.str.contains(search_txt, case=False, na=False)
        ).any(axis=1)
        filtered = filtered[mask]

    if sel_cat_label != "All":
        sel_cat_raw = _label_to_raw(tr.JOB_CAT_VALUE_MAP, sel_cat_label)
        filtered = filtered[filtered["Category"] == sel_cat_raw]

    if sel_diag_label != "All":
        sel_diag_raw = _label_to_raw(tr.JOB_DIAG_VALUE_MAP, sel_diag_label)
        filtered = filtered[filtered["Diagnosis"] == sel_diag_raw]

    # --- 4. DISPLAY TABLE (localized values) ---
    st.write(t("job_matches").format(n=len(filtered)))

    display_df = filtered.copy()
    display_df["Diagnosis"] = display_df["Diagnosis"].apply(
        lambda v: _value_label(tr.JOB_DIAG_VALUE_MAP, v)
    )
    display_df["Category"] = display_df["Category"].apply(
        lambda v: _value_label(tr.JOB_CAT_VALUE_MAP, v)
    )

    display_cols = ["NOC", "Title", "Diagnosis", "Category"]

    st.dataframe(
        display_df[display_cols],
        width='stretch',
        column_config={
            "NOC": st.column_config.TextColumn(t("job_col_noc"), width="small"),
            "Title": t("job_col_title"),
            "Diagnosis": st.column_config.TextColumn(
                t("job_col_diag"), width="medium"
            ),
            "Category": st.column_config.TextColumn(
                t("job_col_cat"), width="medium"
            ),
        },
        hide_index=True,
    )

    # --- 5. VISUAL ANALYSIS (localized category values) ---
    if not display_df.empty:
        with st.expander("📊 " + t("job_cat_chart_title"), expanded=False):
            cat_counts = display_df["Category"].value_counts().reset_index()
            cat_counts.columns = ["Category", "Count"]

            fig = px.bar(
                cat_counts,
                x="Count",
                y="Category",
                orientation="h",
                title=t("job_cat_chart_title"),
                color="Count",
                color_continuous_scale="viridis",
            )
            st.plotly_chart(fig, width='stretch')
