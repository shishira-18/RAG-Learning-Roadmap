from src.config import load_chapters,load_css
from src.utils.content_parser import load_chapter_content   
import streamlit as st
chapters = load_chapters()

def render_chapter_view():
    chapter = next((ch for ch in chapters if ch['id'] == st.session_state.selected_chapter), None)
    
    if chapter:
        # Breadcrumb navigation
        col1, col2, col3 = st.columns([8, 1, 1])
        with col1:
            st.markdown(f"""
            <div class="breadcrumb">
                <a href="#" onclick="return false;">Home</a> 
                <span>›</span> 
                <span>{chapter['number']}: {chapter['title']}</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🚀 Projects"):
                st.session_state.current_view = 'projects'
                st.rerun()
        with col3:
            if st.button("🏠 Home"):
                st.session_state.current_view = 'home'
                st.rerun()
        
        # Chapter content
        st.markdown('<div class="content-area">', unsafe_allow_html=True)
        
        # Load and display chapter content
        content = load_chapter_content(chapter['file'])
        for segment in content:
                if segment["type"] == "text":
                    st.markdown(segment["content"])
                elif segment["type"] == "image":
                    st.image(segment["url"], caption=segment["alt_text"], use_container_width=True, output_format="auto")
        # st.markdown(content)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Navigation buttons
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            current_idx = chapter['id'] - 1
            if current_idx > 0:
                if st.button("← Previous Chapter"):
                    st.session_state.selected_chapter = chapters[current_idx - 1]['id']
                    st.rerun()
        
        with col2:
            st.markdown(f"<center>📚 {chapter['number']} of {len(chapters)}</center>", unsafe_allow_html=True)
        
        with col3:
            if current_idx < len(chapters) - 1:
                if st.button("Next Chapter →"):
                    st.session_state.selected_chapter = chapters[current_idx + 1]['id']
                    st.rerun()