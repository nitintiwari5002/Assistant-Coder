import streamlit as st

st.image("images/image.png", width=100)
st.title("👨🏻‍💻 Assistant Coder: AI That Speaks Your Code.")

lang = st.selectbox("Choose a coding language:", ["Python", "C", "Java", "C++"])

topic = st.text_input("Enter a code required/needed eg(Code for Hello World)...", key="topic_input")

if st.button("Get Code Assistance"):
    from utils.ollama_client import get_info

    if topic.strip() == "":
        st.error("Please enter a valid topic.")
    else:
        with st.spinner("🔎Generating code assistance..."):
            response = get_info(lang,topic)
        st.markdown("### AI Response for your Request is:")
        st.markdown(response)