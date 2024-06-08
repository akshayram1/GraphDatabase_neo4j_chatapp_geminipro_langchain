import streamlit as st
import utils
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.INFO)

# Page configuration
st.set_page_config(page_title="Graph Search Tool", page_icon="🌐", layout="wide")
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0') no-repeat center center fixed;
        background-size: cover;
    }

    .main {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 15px;
        padding: 20px;
        color: white;
    }

    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-size: 16px;
    }

    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: none;
        border-bottom: 2px solid #1f77b4;
        border-radius: 0;
        padding: 8px;
    }

    .stTextInput>div>div>input:focus {
        border-bottom: 2px solid #ff7f0e;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Main container
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("Graph Search Tool")
st.info("I am a Graph Search tool equipped to provide insightful answers by delving into, comprehending, and condensing information from a Graph Database.")
st.sidebar.image("img/globe.png")

# Container setup
reply_container = st.container()
container = st.container()

submit_button = None
user_input = None
with container:
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("Ask a question:", key='input')
        submit_button = st.form_submit_button(label='Send ⬆️')
    
    # Response generation
    if submit_button and user_input:
        result = utils.main(user_input)    
        st.info(result)

st.markdown('</div>', unsafe_allow_html=True)
