import streamlit as st
import streamlit.components.v1 as components

def render(t):
    st.header("📬 Contact & Feedback")

    st.markdown("""
    **Aidez-nous à améliorer cet outil.**

    Si vous avez remarqué une **erreur de calcul**, une **incohérence** avec les règles actuelles,
    ou si vous avez une **suggestion** pour une nouvelle fonctionnalité, merci de nous le signaler ci-dessous.
    """)

    # --- INSTRUCTIONS FOR YOU (THE DEVELOPER) ---
    # 1. Go to Google Forms (forms.google.com) and create a new form.
    # 2. Add fields: Name, Email, Type of Issue (Bug/Suggestion), Message.
    # 3. Click "Send" (Envoyer) -> Click the "< >" (Embed/Intégrer) icon.
    # 4. Copy the 'src' URL from that code (it starts with https://docs.google.com/forms/...)
    # 5. Paste it below in the 'src' variable.

    # REPLACE THIS URL WITH YOUR ACTUAL GOOGLE FORM LINK
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfD_EXAMPLE_LINK_HERE/viewform?embedded=true"

    # This embeds the form directly into the page
    components.iframe(google_form_url, height=800, scrolling=True)
