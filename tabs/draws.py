import streamlit as st
import pandas as pd

# --- Plan d’immigration 2026: Travailleurs qualifiés ---
PLAN_2026_TQ_MIN = 27050
PLAN_2026_TQ_MAX = 29500


def compute_avg_score(draws_data):
    """Average cutoff score across all rows that have a numeric score."""
    df_raw = pd.DataFrame(draws_data)
    if df_raw.empty:
        return 0.0

    scores = pd.to_numeric(df_raw["Score"], errors="coerce")
    scores = scores.dropna()
    if scores.empty:
        return 0.0

    return float(scores.mean())


def _prepare_draws_for_display(draws_data, t):
    """Prepare sorted + translated dataframe for UI display."""
    df = pd.DataFrame(draws_data)

    # --- Translate here ---
    df["Stream"] = df["Stream"].apply(lambda x: t(x))
    df["Notes"] = df["Notes"].apply(lambda x: t(x))

    # Helper sorting field
    df["_Score_sort"] = pd.to_numeric(df["Score"], errors="coerce")

    # Sort: newest date first, then stream name, then higher scores first
    df = df.sort_values(
        ["Date", "Stream", "_Score_sort"],
        ascending=[False, True, False],
    ).reset_index(drop=True)

    df = df.drop(columns=["_Score_sort"])

    # Ensure Invited stays numeric
    df["Invited"] = pd.to_numeric(df["Invited"], errors="coerce")

    # Build a separate display column for Invited (only on first row per Date+Stream)
    seen = set()
    invited_display = []
    for _, row in df.iterrows():
        key = (row["Date"], row["Stream"])
        if key in seen:
            invited_display.append("")
        else:
            invited_display.append(
                "" if pd.isna(row["Invited"]) else str(int(row["Invited"]))
            )
            seen.add(key)

    df["Invited_display"] = invited_display

    # Only show the display column in the UI
    df_display = df[["Date", "Stream", "Score", "Invited_display", "Notes"]].rename(
        columns={"Invited_display": "Invited"}
    )

    return df, df_display




def _compute_summary(draws_data):
    """Compute total invited, average score, and number of draws (date+stream)."""
    df_raw = pd.DataFrame(draws_data)
    if df_raw.empty:
        return 0, 0.0, 0

    # Total invited: sum unique (Date, Stream) so 605/604/649 etc. are not double-counted
    total_invited = (
        df_raw.drop_duplicates(subset=["Date", "Stream"])["Invited"].sum()
    )

    avg_score = compute_avg_score(draws_data)
    num_draws = df_raw.drop_duplicates(subset=["Date", "Stream"]).shape[0]

    return total_invited, avg_score, num_draws


def render(draws_data, t):
    st.write(f"### {t('draws_title')}")
    st.write(t('draws_sub'))

    # ---- Summary metrics (top) ----
    total_invited, avg_score, num_draws = _compute_summary(draws_data)

    # Compare to Plan d’immigration 2026 – Travailleurs qualifiés
    used = total_invited
    remaining_min = max(PLAN_2026_TQ_MIN - used, 0)
    remaining_max = max(PLAN_2026_TQ_MAX - used, 0)

    used_pct_min = used / PLAN_2026_TQ_MAX * 100  # vs max
    used_pct_max = used / PLAN_2026_TQ_MIN * 100  # vs min

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(t("total_invited"), f"{total_invited:,}")
    with c2:
        st.metric(t("average_cutoff"), f"{avg_score:.1f}")
    with c3:
        min_str = f"{PLAN_2026_TQ_MIN:,}"
        max_str = f"{PLAN_2026_TQ_MAX:,}"
        st.metric(
            t("plan_2026_metric_label"),
            f"{remaining_min:,} – {remaining_max:,}",
            help=t("plan_2026_metric_help").format(min=min_str, max=max_str),
        )
        st.caption(
            t("plan_2026_caption").format(
                pct_min=f"{used_pct_min:.1f}",
                pct_max=f"{used_pct_max:.1f}",
            )
        )

    # ---- Single main table, no manual pagination ----
    _, df_display = _prepare_draws_for_display(draws_data, t)

    st.dataframe(
        df_display,
        width="stretch",
        hide_index=True,
    )

    st.caption(t("draws_table_caption"))

    # --- References ---
    with st.expander(t("draws_ref_title")):
        st.markdown(t("draws_ref_body"))

    st.info(t('tip'))
