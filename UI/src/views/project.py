from src.config import load_chapters
from src.utils.ui_components import render_project_card
import streamlit as st

chapters = load_chapters()
def render_projects_view():
    chapter = next((ch for ch in chapters if ch['id'] == st.session_state.selected_chapter), None)
    
    if chapter:
        # Breadcrumb
        col1, col2 = st.columns([10, 2])
        with col1:
            st.markdown(f"""
            <div class="breadcrumb">
                <a href="#" onclick="return false;">Home</a> 
                <span>›</span> 
                <span>{chapter['number']}</span>
                <span>›</span> 
                <span>Projects</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("← Back"):
                st.session_state.current_view = 'home'
                st.rerun()
        
       
        
        # Display projects
        for project in chapter['projects']:
            render_project_card(project, chapter['id'])
            
        if not chapter['projects']:
            st.info("No projects available for this chapter yet.")