import streamlit as st
from model_training_service import Code

def app():
        
    # Creating an object of prediction service
    pred = Code()

    api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

    # Using the streamlit cache 
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input, api_key=api_key)
    
    if api_key:
            
        # Setting up the Title
        st.title("đšī¸ Blog Generater ")
        st.write(" This API powered app will generate text for blog ")
        st.write(f"""---""")

        input = st.text_input('Input:')

        if st.button('Submit'):
            st.write('**Output**')
            st.write(f"""---""")
            with st.spinner(text='In progress'):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("đ API Key Not Found!")
        st.info("đĄ Copy paste your OpenAI API key that you can find in User -> API Keys section once you log in to the OpenAI API Playground")
