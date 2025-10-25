import streamlit as st

def render_project_card(project, chapter_id):
    st.markdown(f'<div class="project-card-v2">', unsafe_allow_html=True)
    with st.container(border=True):
        header_col1, header_col2 = st.columns([4, 1])

        with header_col1:
            st.markdown(f"**<span class='project-title-v2'>🚀 {project['title']}</span>**", unsafe_allow_html=True)
            st.markdown(f"<span class='project-stats-v2'>⚡ {project['difficulty']} &nbsp; | &nbsp; ⏱️ {project['time']}</span>", unsafe_allow_html=True)
        
        with header_col2:
            # We add a class to the button container for vertical centering in CSS
            st.markdown('<div class="button-aligner">', unsafe_allow_html=True)
            if st.button("Open", type="primary", key=f"proj_{project['id']}"):
                # Open should go directly to chat-only view
                st.session_state.selected_project = project
                st.session_state.selected_chapter = chapter_id
                st.session_state.current_view = 'project_chat'
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with st.expander("Read Details"):
            st.markdown(f"""
            <div class='project-description-v2'>
                {project['description']}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
