import streamlit as st
import pandas as pd


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
            invited_display.append("")  # visually empty, underlying numeric stays in Invited
        else:
            # you can format with thousands separator if you want
            invited_display.append(str(int(row["Invited"])) if pd.notna(row["Invited"]) else "")
            seen.add(key)

    df["Invited_display"] = invited_display

    # Only show the display column in the UI
    df_display = df[["Date", "Stream", "Score", "Invited_display", "Notes"]].rename(
        columns={"Invited_display": "Invited"}
    )

    return df, df_display  # df = raw (with numeric Invited), df_display = for UI


def _compute_summary(draws_data):
    """Compute total invited and average score (only where a score exists)."""
    df_raw = pd.DataFrame(draws_data)
    if df_raw.empty:
        return 0, 0.0, 0

    # Total invited: sum unique (Date, Stream) so 605/604/649 are not double-counted
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

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Total invited (all draws)", f"{total_invited:,}")
    with c2:
        st.metric("Average cutoff score (Streams 1–3)", f"{avg_score:.1f}")

    # ---- Single main table, no manual pagination ----
    _, df_display = _prepare_draws_for_display(draws_data)

    st.dataframe(
        df_display,
        width="stretch",
        hide_index=True,
    )

    st.caption(
        "Each row is a published score cutoff within a draw. For Stream 4 "
        "(Exceptional talent), no score cutoff is published, so the score cell is empty. "
        "“Invited” is the total invitations for that date and stream, shown only on the "
        "first line for each draw."
    )

    st.info(t('tip'))
