import streamlit as st

Home = st.Page("pages/Home.py", title = "Home")
personal = st.Page("pages/Info.py", title = "Personal AI Assistant")
About = st.Page("pages/About.py", title = "About")
pg = st.navigation([Home , personal, About], position = "top")

pg.run()