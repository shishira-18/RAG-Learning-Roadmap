from src.config import load_chapters
from src.utils.ui_components import render_project_card
import streamlit as st
import subprocess
import sys
import os
from dotenv import load_dotenv

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


def render_project_view():
    """Render a single project detail page and allow running the project script.

    For now this maps known project IDs to local script files and runs them using
    the current Python interpreter. Output is captured and displayed.
    """
    project = st.session_state.get('selected_project')
    chapter_id = st.session_state.get('selected_chapter')

    if not project:
        st.warning("No project selected.")
        return

    # Breadcrumb + back button
    col1, col2 = st.columns([10, 2])
    with col1:
        st.markdown(f"""
        <div class="breadcrumb">
            <a href="#" onclick="return false;">Home</a>
            <span>›</span>
            <a href="#" onclick="return false;">{chapter_id and ('Chapter ' + str(chapter_id)) or ''}</a>
            <span>›</span>
            <span>{project['title']}</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("← Back"):
            st.session_state.current_view = 'projects'
            st.rerun()

    st.markdown(f"## 🚀 {project['title']}")
    st.markdown(f"**Difficulty:** {project.get('difficulty','-')}  •  **Estimated time:** {project.get('time','-')}")
    st.markdown("---")
    st.markdown(project.get('description',''))

    st.markdown("---")

    # Determine script path for known projects
    script_path = None
    # Map chapter 1, project p1 to basic_rag_chatbot.py
    if chapter_id == 1 and project.get('id') == 'p1':
        script_path = os.path.join(os.getcwd(), 'projects', 'chapter_1', 'basic_rag_chatbot.py')

    if not script_path or not os.path.exists(script_path):
        st.info("No runnable script is configured for this project.")
        return

    # Run controls
    run_col, out_col = st.columns([1, 3])
    with run_col:
        if st.button("Run Project"):
            st.session_state['project_output'] = ""  # reset
            try:
                with st.spinner("Running project — this may take a few seconds"):
                    proc = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                    output, _ = proc.communicate(timeout=180)
                    st.session_state['project_output'] = output
            except subprocess.TimeoutExpired:
                proc.kill()
                st.session_state['project_output'] = "Execution timed out."
            except Exception as e:
                st.session_state['project_output'] = f"Error running script: {e}"

    # Display output
    out = st.session_state.get('project_output')
    if out is not None:
        st.markdown("### Output")
        st.code(out)

    # End of render_project_view


def render_project_chat():
    """Render chat-only view for a selected project.

    Clicking Open will route here and show only the chat window.
    """
    project = st.session_state.get('selected_project')
    hist_key = f"chat_history_{project.get('id')}"
    if hist_key not in st.session_state:
        st.session_state[hist_key] = []

    # Header row: title + controls (Clear Chat, Back)
    cols = st.columns([6, 1, 1])
    with cols[0]:
        st.markdown(f"**{project.get('title','') }**")
    # Clear chat button (right-aligned)
    with cols[1]:
        if st.button('Clear Chat', key=f'clear_{project.get("id")}'):
            st.session_state[hist_key] = []
            # show a small confirmation and continue rendering so Back remains visible
            st.success("Chat cleared")
    # Back button
    with cols[2]:
        if st.button('← Back', key=f'back_{project.get("id")}'):
            st.session_state.current_view = 'projects'
            st.rerun()

    # Render existing messages using st.chat_message
    for role, text in st.session_state[hist_key]:
        # Streamlit expects roles 'user' and 'assistant'
        msg_role = 'assistant' if role == 'bot' else 'user'
        with st.chat_message(msg_role):
            st.write(text)

    # Input using native chat_input (simpler UX)
    user_input = st.chat_input("Ask the chatbot...")
    if user_input:
        # Append user message and render it
        st.session_state[hist_key].append(('user', user_input))
        with st.chat_message('user'):
            st.write(user_input)

        # Call the model and show assistant reply
        try:
            load_dotenv()
            from google import genai
            client = genai.Client(api_key=os.getenv('GEMINI_KEY'))
            with st.spinner('Generating response...'):
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                )
            bot_text = getattr(response, 'text', str(response))
        except Exception as e:
            bot_text = f"Error: {e}"

        st.session_state[hist_key].append(('bot', bot_text))
        with st.chat_message('assistant'):
            st.write(bot_text)