import streamlit as st
from src.config import load_chapters
chapters = load_chapters()
def render_homepage_view():
    st.markdown("# 📚 RAG Mastery Hub")
    st.markdown("### Your comprehensive guide to Retrieval-Augmented Generation")
    st.markdown("---")
    
    # Chapter cards
    for chapter in chapters:
        st.markdown(f"""
        <div class="chapter-card">
            <span class="chapter-number">{chapter['number']}</span>
            <div class="chapter-title">{chapter['title']}</div>
            <div class="chapter-description">{chapter['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1,gap, col2 = st.columns([1,3.5, 1])
        with col1:
            if st.button(f"📖 Read Chapter", key=f"read_{chapter['id']}"):
                st.session_state.selected_chapter = chapter['id']
                st.session_state.current_view = 'chapter'
                st.rerun()
        with col2:
            if st.button(f"🚀 View Projects", key=f"proj_view_{chapter['id']}"):
                st.session_state.selected_chapter = chapter['id']
                st.session_state.current_view = 'projects'
                st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)