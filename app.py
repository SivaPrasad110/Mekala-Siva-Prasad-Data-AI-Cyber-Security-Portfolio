import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Mekala Siva Prasad | Data • AI • Cyber Security",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        margin: 0;
        padding: 0;
    }

    .block-container {
        padding: 0;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Load portfolio HTML
html_file = Path(__file__).parent / "index.html"

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")

    components.html(
        html_content,
        height=5000,
        scrolling=True
    )
else:
    st.error("index.html was not found in the repository.")
