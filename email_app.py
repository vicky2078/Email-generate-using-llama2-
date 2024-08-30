import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def getLLMResponse(form_input,email_sender,email_recipient,email_style):
    llm = CTransformers(model='llama-2-13b-chat.ggmlv3.q2_K.bin',
                    model_type='llama',
                    config={'max_new_tokens': 256,
                            'temperature': 0.01})
    
    
    template = """
    Write a email with {style} style and includes Topic :{email_topic}.\n\nSender: {sender}\Receiver: {recipient}
    \n\nEmail Text:
    
    """

    prompt = PromptTemplate(
    input_variables=["style","email_topic","sender","recipient"],
    template=template,)

  
    #Generating the response using LLM
    response=llm(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))
    print(response)

    return response


st.set_page_config(page_icon='📧',
                    page_title="Generate Emails",
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("📧 AutoMail")

col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input('Name of the Sender')
with col2:
    email_recipient = st.text_input('Name of the Receiver')
with col3:
    email_style = st.selectbox('Style of Writing',
                                    ('Formal', 'Neutral', 'Appreciating', 'Not Satisfied'),
                                       index=0)

form_input = st.text_area('Write a Gist regarding what the E-Mail is about:', placeholder="Today I won the Chess Tournament", height=250)


submit = st.button("Generate")

if submit:
    st.write(getLLMResponse(form_input,email_sender,email_recipient,email_style))