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


def _prepare_draws_for_display(draws_data):
    """Return a DataFrame for display. Keep Invited numeric, add a string display column."""
    df = pd.DataFrame(draws_data)

    # Helper column for sorting scores (None -> NaN)
    df["_Score_sort"] = pd.to_numeric(df["Score"], errors="coerce")

    # Sort: newest date first, then stream name, then higher scores first
    df = df.sort_values(
        ["Date", "Stream", "_Score_sort"],
        ascending=[False, True, False],
    ).reset_index(drop=True)

    df = df.drop(columns=["_Score_sort"])

    # Ensure Invited stays numeric
    df["Invited"] = pd.to_numeric(df["Invited"], errors="coerce")

    # Build a separate display column for Invited
    seen = set()
    invited_display = []
    for _, row in df.iterrows():
        key = (row["Date"], row["Stream"])
        if key in seen:
            invited_display.append("")  # visually empty
        else:
            invited_display.append(
                str(int(row["Invited"])) if pd.notna(row["Invited"]) else ""
            )
            seen.add(key)

    df["Invited_display"] = invited_display

    # Only show the display column in the UI
    df_display = df[["Date", "Stream", "Score", "Invited_display", "Notes"]].rename(
        columns={"Invited_display": "Invited"}
    )

    return df, df_display  # df = raw, df_display = for UI


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

    # Compare to Plan d’immigration 2026 – Travailleurs qualifiés (27 050 – 29 500)
    used = total_invited
    remaining_min = max(PLAN_2026_TQ_MIN - used, 0)
    remaining_max = max(PLAN_2026_TQ_MAX - used, 0)

    # Share of the 2026 plan already "used" by current PSTQ selections
    used_pct_min = used / PLAN_2026_TQ_MAX * 100  # vs max
    used_pct_max = used / PLAN_2026_TQ_MIN * 100  # vs min

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total invited (PSTQ Streams 1–4)", f"{total_invited:,}")
    with c2:
        st.metric("Average cutoff score (Streams 1–3)", f"{avg_score:.1f}")
    with c3:
        st.metric(
            "Estimated places remaining (Plan 2026 – Travailleurs qualifiés)",
            f"{remaining_min:,} – {remaining_max:,}",
            help=(
                "Based on Québec’s Plan d’immigration 2026 for Travailleurs qualifiés "
                f"({PLAN_2026_TQ_MIN:,}–{PLAN_2026_TQ_MAX:,}). "
                "PSTQ selections made in 2025 are assumed to contribute primarily "
                "to 2026 admissions. This comparison is indicative."
            ),
        )
        st.caption(
            f"Current selections ≈ {used_pct_min:.1f}–{used_pct_max:.1f}% of the 2026 "
            "Travailleurs qualifiés plan."
        )

    # ---- Single main table, no manual pagination ----
    _, df_display = _prepare_draws_for_display(draws_data)

    st.dataframe(
        df_display,
        width="stretch",
        hide_index=True,
    )

    st.caption(
        "Each row is a published score cutoff within a draw. For Stream 4 "
        "(Exceptional talent), no score cutoff is published. "
        "“Invited” is the total invitations for that date and stream. "
        "The quota comparison is a forward-looking estimate against the "
        "2026 Travailleurs qualifiés admission plan."
    )

    # --- References ---
    with st.expander("References and sources"):
        st.markdown(
            "- [Plan d’immigration 2026 – MIFI (official PDF)]"
            "(https://cdn-contenu.quebec.ca/cdn-contenu/adm/min/immigration/publications-adm/plan-immigration/PL_immigration_2026_MIFI.pdf"
            ")\n"
            "- [PSTQ Invitations dans Arrima du Programme de sélection des travailleurs qualifiés (2025)]"
            "(https://www.quebec.ca/immigration/permanente/travailleurs-qualifies/programme-selection-travailleurs-qualifies/invitation/2025)"
        )

    st.info(t('tip'))

