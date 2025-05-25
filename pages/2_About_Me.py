import streamlit as st
from sidebar_utils import render_sidebar
import time
import numpy as np

render_sidebar()

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.title("About Me")
    st.write("""I'm a recent graduate from Berry College with a B.S. in Data Analytics and a minor in Computer Science. During my time at Berry College, I 
                developed a strong technical foundation in Python, R, SQL, machine learning, data analysis, and data visualization through both coursework 
                and a hands-on internship experience. My passions are simple: Turning raw data into actionable insights, developing visualizations that tell 
                simple but powerful stories, machine learning, and learning new skills. Whether it's picking up a new tool, exploring an unfamiliar data, or learning new technologies,
                I'm a fast learner who thrives on expanding my skill set and applying new knowledge to real-world problems.
            """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("My Skills")
    st.markdown("""
    - **Languages**: Python, SQL, R, Java, Stata
    - **Machine Learning and Data Science**: Pandas, NumPy, Scikit-learn, PyTorch, TensorFlow, Keras, NLP 
    - **Data Analysis & Visualization**: Microsoft Power BI, Google Analytics, Salesforce Marketing Cloud, RStudio, Tableau
    - **Microsoft Tools**: Excel, PowerPoint, Office Suite
    - **Misc/Tools**: Git, Jupyter Notebooks, Google Colab, VS Code
    """)
    
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.subheader("My Coursework and Experience")
    st.write("""At Berry College, I took many valuable courses. These courses include (but are not limited to):""")
    st.markdown("""
                - **Data Analytics**: Business Analytics, Business Intelligence and Information Systems, Data Visualization, Intermediate Data Analytics
                - **Machine Learning and Data Science**: Data Management and Data Science, Machine Learning
                - **Programming**: Data Structures and Algorithms, Object-Oriented Program Design
                - **Statistics and Research**: Business Statistics, Elementary Statistics, Econometrics
                """)
    st.write("""These courses gave me hands-on experience with Python, R, SQL, machine learning, data analysis, and data visualization. They also shaped the way 
             I approach problems, teaching me to think critically with data, build effective models, and communicate insights.""")

    st.subheader("Data Analyst Internship (Feb 2024 - Aug 2024)")

    st.write("""During my junior year I had an internship at Berry as a Data Analyst for the Digital Tactics and Marketing Department. In this role, I analyzed several 
             years of admissions, marketing, and email campaign data to uncover trends and provide actionable insights on the effectiveness of the department's outreach 
             and marketing strategies. One of the biggest contributions I made was offering a direct student perspective to a team that was technically strong but new to applying 
             data analytics in a higher education field. While they understood the data, they were interpreting it without much input from actual students. I helped 
             fill that gap by giving real-world context, such as what messaging lands well with students, what doesn't, and how students typically engage with emails and 
             campaigns.""")
    st.write("Below are some more accomplishments I had in the role:")
    st.markdown("""
                - Analyzed multiple years of admissions and marketing data as well as email campaigns, generating metrics and KPIs such as click-through rates, 
                click-to-open rates, and bounce rates
                - Developed comprehensive dashboards in Microsoft Power BI, providing actionable insights and data-driven recommendations for future email and marketing campaigns
                - Generated detailed pivot tables in Microsoft Excel to extract KPIs, driving strategic decisions based on email campaign performance
                - Prepared presentations and reports to present my findings post-analysis
                - Established a shared glossary for our team and the departments we collaborated with to ensure clear communication across departments
                """)
    
    st.subheader("Resident Assistant (May 2023 - May 2025)")
    st.write("""For two years I worked on-campus as a Resident Assistant for Residence Life. While this role did help me grow professionally, it helped me grow more personally.
             When I first came to Berry College, I was not much of a people person and I was definitely not a leader. If you had told me freshman year that I would've been
             a resident assistant, I would've laughed. Becoming a resident assistant though helped me in many ways that I did not expect. I developed stronger interpersonal
             skills, learned how to relate to those with different backgrounds from my own, de-escalate conflicts, and manage a hall of over 40+ students. I also improved my time 
             management skills. As an RA, we have a lot of deadlines to meet throughout the year. We had to put on five programs a semester, sit two desk shifts a week, multiple shifts 
             on weekends, go to meetings, do resident check-ins, etc. These requirements forced me to be better about time management and meeting deadlines.""")
    st.write("Below are some more accomplishments I had in the role:")
    st.markdown("""
                - Planned and hosted hall programs for students to get to know one another in a safe environment
                - Created eye-catching bulletin boards to display different campus-wide events, hall programs, important information, and important dates to be on students' radars
                - Oversaw the well-being of the hall including maintenance issues, conflict management, and sitting at the front desk to assist in any way possible such as lockouts
                - Assisted in supervising residents and responding to complaints, reports, requests, and emergencies
                """)