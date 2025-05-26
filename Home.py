import streamlit as st
from sidebar_utils import render_sidebar

st.set_page_config(page_title="Portfolio", layout="wide")

render_sidebar()

st.markdown(
    """
    <div style='display: flex; flex-direction: column; align-items: center; justify-content: center;'>
        <img src='https://raw.githubusercontent.com/nov8r/Portfolio/static/Headshot-Resized.jpg' width='200' style='border-radius: 8%; margin-bottom: 5px;'/>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("Hi, I'm Ethan! 👋")
    st.markdown("""I'm a recent graduate from Berry College with a B.S. in Data Analytics and a minor in Computer Science. My passions are simple: 
                Turning raw data into actionable insights, developing visualizations that tell simple but powerful stories, machine learning, and learning new skills.
                """)
    st.markdown("""Feel free to connect with me via [LinkedIn](https://linkedin.com/in/ethanposey)  
                or email me at `ethanposeyk@outlook.com`
                """)
    st.info("📌 Use the sidebar to explore my projects and learn more about me!")
