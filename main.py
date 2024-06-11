import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Set the page configuration
st.set_page_config(
    page_title="T-Shirts Database Q&A",
    page_icon="👕",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Apply custom CSS styles including Google Fonts
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

    body {
        background-color: #f4f4f9;
        color: #333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: auto;
    }
    .stTextInput label {
        color: #000;
        font-size: 16px;
    }
    .stTextInput input {
        background-color: #ffffff;
        color: #000;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #ddd;
        width: 100%;
        margin-bottom: 10px;
        font-size: 16px;
    }
    .stButton button {
        background-color: #007BFF;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px 2px;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .title {
        text-align: center;
        font-size: 3em;
        color: #333;
        margin-top: 20px;
        font-family: 'Lobster', cursive;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        color: #666;
        margin-bottom: 30px;
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 0.9em;
        color: #777;
    }
    .spinner {
        text-align: center;
        color: #007BFF; /* Same color as the loading circle */
        font-size: 1.2em;
    }
    .answer {
        color: #008000;
        font-size: 1.2em;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a heading and description
st.markdown("<div class='title'>T-Shirts Database Q&A 👕</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='description'>Welcome! Ask any question about our T-shirts database, and our AI will provide the answer using advanced SQL query generation. Just type your question below and hit Enter.</div>",
    unsafe_allow_html=True,
)

# Input section
question = st.text_input("Enter your question here:")

if question:
    # Create a placeholder for the spinner
    spinner_placeholder = st.empty()

    with spinner_placeholder:
        with st.spinner(text=""):
            spinner_placeholder.markdown("<div class='spinner'>Fetching the answer...</div>", unsafe_allow_html=True)
            # Run the query and get the response
            chain = get_few_shot_db_chain()
            response = chain.run(question)

    # Clear the spinner and display the answer
    spinner_placeholder.empty()
    st.markdown("<div class='answer'><strong>Answer:</strong><br>" + response + "</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <footer class='footer'>
        <hr>
        <p>© 2024 TOUFIQUE HASAN</p>
    </footer>
    """,
    unsafe_allow_html=True
)
