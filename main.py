import streamlit as st
import langchain_helper as lch
import textwrap

st.title("Edu Query: 📚🧑‍🎓👨🏻‍🎓⏱️💻⏳")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label = "What is the YouTube video URL?",
            max_chars = 50
        )
        query = st.sidebar.text_area(
            label = "Ask me about the video?",
            max_chars = 50
        )
        submit_buttom = st.form_submit_button(label='Submit')
        
if youtube_url and query:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response = lch.get_response_from_query(db,query)
    # answer = response + "/n" + docs + "/n" 
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=80))
    


