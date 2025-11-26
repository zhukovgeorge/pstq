import streamlit as st
import pandas as pd

def render(draws_data, t):
    st.write(f"### {t('draws_title')}")
    st.write(t('draws_sub'))

    draws_df = pd.DataFrame(draws_data)
    st.dataframe(draws_df, width='stretch', hide_index=True) # Use 'stretch' for consistency

    st.info(t('tip'))
