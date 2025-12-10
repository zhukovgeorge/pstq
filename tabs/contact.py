import streamlit as st
import streamlit.components.v1 as components

def render(t):
    st.header("📬 Contact & Feedback")

    st.markdown("""
    **Aidez-nous à améliorer cet outil.**

    Si vous avez remarqué une **erreur de calcul**, une **incohérence** avec les règles actuelles,
    ou si vous avez une **suggestion** pour une nouvelle fonctionnalité, merci de nous le signaler ci-dessous.
    """)
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSclc5YQk3wDX_ynThXNyUxJOA5uVCWPt8DulBbo_LKr5iT1XA/viewform?usp=dialog/viewform?embedded=true"
    components.iframe(google_form_url, height=1000, scrolling=True)
