import streamlit as st

def render_sidebar():
    st.sidebar.markdown(
        f"""
        <div style="text-align: center;">
            <p style="font-size: 14px; margin-bottom: 0.1rem;"><a href="mailto:ethanposeyk@outlook.com">ethanposeyk@outlook.com</a></p>
            <p style="font-size: 14px; margin-bottom: 0.1rem;"><a href="https://www.linkedin.com/in/ethanposey" target="_blank">LinkedIn</a></p>
            <p style="font-size: 14px;"><a href="https://www.github.com/nov8r" target="_blank">GitHub</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )