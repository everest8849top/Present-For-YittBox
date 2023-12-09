import os
import random
import streamlit as st

#decorator
def enable_chat_history(func):
    if st.secrets['OPENAI_API_KEY']:

        # to clear chat history after swtching chatbot
        # current_page = func.__qualname__
        # if "current_page" not in st.session_state:
        #     st.session_state["current_page"] = current_page
        # if st.session_state["current_page"] != current_page:
        #     try:
        #         st.cache_resource.clear()
        #         del st.session_state["current_page"]
        #         del st.session_state["messages"]
        #     except:
        #         pass

        # to show chat history on ui
        if "messages" not in st.session_state:
            with open("document.txt") as file:
                qa = file.read()
            st.session_state["messages"] = [
                {"role" : "system", "content" : f"Your name is Vladyslav Lopuha, and you gotta represent my idea to Yittbox!\
                 Please reference this.\
                 Remember! I'll provide the sample questions and answers and please reference them to represent me!\
                 For example if the user ask 'How do you think about the company?', and then you can answer 'It's a powerful company where I want to enter.'.\
                 Here's the questions and answers.\
                 {qa}"},
                {"role": "assistant", "content": "Hello, my name is Vladyslav. I'll represent my opinion to your company and I'll introduce about myself."},
                {"role" : "user", "content" : "How do you think about Yittbox?"},
                {"role" : "assistant", "content" : "It's a powerful company where I want to enter."}
            ]
        for msg in st.session_state["messages"]:
            if msg['role'] != 'system':
                st.chat_message(msg["role"]).write(msg["content"])

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute

def display_msg(msg, author):
    """Method to display message on the UI

    Args:
        msg (str): message to display
        author (str): author of the message -user/assistant
    """
    st.session_state.messages.append({"role": author, "content": msg})
    st.chat_message(author).write(msg)

def configure_openai_api_key():
    return st.secrets['OPENAI_API_KEY']