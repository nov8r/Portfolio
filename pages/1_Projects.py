import streamlit as st
from sidebar_utils import render_sidebar

render_sidebar()

st.title("Projects")
st.markdown("""
Below are some of the data analytics, data science, and machine learning projects I've worked on.
""")

# Tabs for each project
tabs = st.tabs(["📊 EDA on Caffeine Drinks", 
                "🦊 Animal Image Classification using CNNs", 
                "🦠 Breast Cancer Diagnosis Prediction Model"])

# Project 1: Caffeine EDA
with tabs[0]:
    st.header("📊 EDA on Caffeine Drinks")
    st.write("An exploratory analysis of caffeine content across various drinks to find patterns in energy-level claims.")
    st.markdown("""
    **Tools Used:** pandas, matplotlib, seaborn  
    **GitHub:** [EDA-Caffeine](https://github.com/yourusername/caffeine-eda)  
    **Live Demo:** Coming Soon!
    """)
    st.write("Key findings include grouping by drink type and linking caffeine density to brand positioning.")

# Project 2: Animal Classification ML Model
with tabs[1]:
    st.header("🦊 Animal Image Classification using CNNs")
    st.write("Trained an in-depth CNN architecture on the Animals-10 dataset using BCE loss.")
    st.markdown("""
    **Tools Used:** PyTorch, Scikit-Learn, Matplotlib, TQDM   
    **GitHub:** [Animal-Classification](https://github.com/nov8r/Animal-Classification)  
    """)
    st.write("Achieved ~95% accuracy on cross-validated pairs with visual similarity scoring.")

# Project 3: Breast Cancer Diagnosis Prediction Model
with tabs[2]:
    st.header("🦠 Breast Cancer Diagnosis Prediction Model")
    st.write("Trained several machine learning models including Neural Nets, SVM, Random Forest, etc. to predict the diagnosis (malignant or benign) of a tumor based on the physical characterisitics of the tumor.")
    st.markdown("""
    **Tools Used:** Pandas, NumPy, Scikit-Learn, Matplotlib   
    **GitHub:** [Breast-Cancer-ML](https://github.com/nov8r/Breast-Cancer-Prediction)  
    """)
    st.write("Achieved ~92%+ across all key performance metrics for each model")

st.markdown("---")
st.markdown("📫 **Contact**: [ethanposeyk@outlook.com](mailto:ethanposeyk@outlook.com) | [LinkedIn](https://linkedin.com/in/ethanposey)")
