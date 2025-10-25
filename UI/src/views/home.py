import streamlit as st
from src.config import load_chapters

chapters = load_chapters()


def render_homepage_view():
    # Hero section
    st.markdown(
        """
    <div class="hero">
      <div class="hero-inner">
        <h1>📚 RAG Mastery Hub</h1>
        <p class="lead">A practical, hands-on roadmap to mastering Retrieval-Augmented Generation — learn concepts, read chapters, and build projects.</p>
      </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # CTA buttons centered under hero
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        col_a, col_b = st.columns(2, gap="small")
        with col_a:
            if st.button("📖 Start Learning", key="cta_start"):
                st.session_state.current_view = "chapter"
                st.session_state.selected_chapter = chapters[0]["id"] if chapters else None
                st.rerun()
        with col_b:
            if st.button("🚀 Explore Projects", key="cta_projects"):
                st.session_state.current_view = "projects"
                st.session_state.selected_project = None
                st.rerun()

    st.markdown("---")

    # Chapter grid — 3 columns responsive
    def chunk(lst, n):
        for i in range(0, len(lst), n):
            yield lst[i : i + n]

    for row in chunk(chapters, 3):
        cols = st.columns(3, gap="large")
        for idx, chapter in enumerate(row):
            with cols[idx]:
                # Card HTML (visual only)
                st.markdown(
                    f"""
                <div class="chapter-card">
                  <div style="display:flex;align-items:center;justify-content:space-between;">
                    <div>
                      <div class="chapter-number">{chapter['number']}</div>
                      <div class="chapter-title">{chapter['title']}</div>
                    </div>
                    <div style="font-size:28px;opacity:0.85">📘</div>
                  </div>
                  <div class="chapter-description">{chapter['description']}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                # Action buttons for each chapter (keeps original behavior)
                b1, b2 = st.columns([1, 1], gap="small")
                with b1:
                    if st.button("📖 Read", key=f"read_{chapter['id']}"):
                        st.session_state.selected_chapter = chapter["id"]
                        st.session_state.current_view = "chapter"
                        st.rerun()
                with b2:
                    if st.button("🔧 Projects", key=f"proj_view_{chapter['id']}"):
                        st.session_state.selected_chapter = chapter["id"]
                        st.session_state.current_view = "projects"
                        st.rerun()

        # small spacer between rows
        st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)