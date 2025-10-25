import streamlit as st
from src.config import load_chapters,load_css
from src.views.home import render_homepage_view
from src.views.chapter import render_chapter_view
from src.views.project import render_projects_view


# Page configuration
st.set_page_config(
    page_title="RAG Mastery Hub", 
    layout="wide",
    initial_sidebar_state="expanded"
)
custom_css = load_css()
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)


# Initialize session state
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'home'
if 'selected_chapter' not in st.session_state:
    st.session_state.selected_chapter = None
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None

# Main content area
if st.session_state.current_view == 'home':
    # Home page - Chapter selection
    render_homepage_view()

elif st.session_state.current_view == 'chapter':
    # Chapter reading view
    render_chapter_view()

elif st.session_state.current_view == 'projects':
    # Projects view for selected chapter
    render_projects_view()

# Footer
st.markdown("---")
st.markdown("""
<center>
    <small>
        RAG Mastery Hub • Built with ❤️ for the community<br>
        <a href="https://github.com/shishira-18/RAG-Learning-Roadmap.git">GitHub</a> • 
        <a href="ksshishira01@gmail.com">Contact</a>
    </small>
</center>
""", unsafe_allow_html=True)