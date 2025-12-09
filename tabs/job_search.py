import streamlit as st
import pandas as pd
import plotly.express as px
import job_data

def render():
    st.header("🕵️ Job Market Intelligence")
    st.markdown("""
    **Goal:** Identify if your profession is in **Deficit** (High Points).
    *Data Source: Official Govt. Diagnostics*
    """)

    # --- 1. LOAD DATA ---
    df_jobs = pd.DataFrame(job_data.JOBS)

    # --- 2. DASHBOARD STATS ---
    deficit_count = len(df_jobs[df_jobs['Diagnosis'].str.contains("Déficit", na=False)])
    st.metric("Total Deficit Professions", deficit_count, delta="High Priority Targets")

    st.divider()

    # --- 3. SEARCH & FILTERS ---
    col_search, col_cat, col_diag = st.columns([2, 1, 1])

    search_txt = col_search.text_input("🔍 Search Job Title or NOC", placeholder="e.g. Software, 21232")

    cat_opts = ["All"] + sorted(df_jobs['Category'].unique().tolist())
    sel_cat = col_cat.selectbox("Category", cat_opts)

    diag_opts = ["All"] + sorted(df_jobs['Diagnosis'].dropna().unique().tolist())
    sel_diag = col_diag.selectbox("Diagnosis", diag_opts)

    # Apply Filters
    filtered = df_jobs.copy()

    if search_txt:
        mask = filtered.astype(str).apply(lambda x: x.str.contains(search_txt, case=False, na=False)).any(axis=1)
        filtered = filtered[mask]

    if sel_cat != "All":
        filtered = filtered[filtered['Category'] == sel_cat]

    if sel_diag != "All":
        filtered = filtered[filtered['Diagnosis'] == sel_diag]

    # --- 4. DISPLAY TABLE ---
    st.write(f"Showing **{len(filtered)}** matches:")

    st.dataframe(
        filtered,
        width='stretch',
        column_config={
            "NOC": st.column_config.TextColumn("Code", width="small"),
            "Title": "Job Title",
            "Diagnosis": st.column_config.TextColumn("Status", width="medium"),
            "Category": st.column_config.TextColumn("Category", width="medium"),
        },
        hide_index=True
    )

    # --- 5. VISUAL ANALYSIS ---
    if not filtered.empty:
        with st.expander("📊 View Category Analysis", expanded=False):
            cat_counts = filtered['Category'].value_counts().reset_index()
            cat_counts.columns = ['Category', 'Count']

            fig = px.bar(
                cat_counts,
                x='Count',
                y='Category',
                orientation='h',
                title="Distribution of Jobs by Category (Filtered)",
                color='Count',
                color_continuous_scale="viridis"
            )
            st.plotly_chart(fig, width='stretch')
