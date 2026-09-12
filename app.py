import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Mekala Siva Prasad — Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stAppViewContainer"] > .main {padding: 0 !important;}
[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}
iframe {border: 0 !important;}
</style>
""", unsafe_allow_html=True)

html_path = Path(__file__).parent / "index.html"

if not html_path.exists():
    st.error("Portfolio file not found: index.html")
    st.stop()

html = html_path.read_text(encoding="utf-8")

components.html(
    html,
    height=6500,
    scrolling=True,
)
