import streamlit as st

st.set_page_config(
    page_title="Blog Generator",
    page_icon="🐾",
    layout="centered")

# Pages as key-value pairs
PAGES = {
    "Blog Generator": app2
}

st.sidebar.title('Go to:')

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
