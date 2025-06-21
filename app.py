import streamlit as st
from navbar.navbar import render_navbar
from hero.hero import render_hero
from footer.footer import render_footer

# Set page config
st.set_page_config(page_title="Diamond Shopping Mall", layout="wide")

# Load styles
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Render sections
render_navbar()
render_hero()
render_footer()

