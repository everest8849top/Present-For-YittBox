import os
import utils
import streamlit as st

from openai import OpenAI
client = OpenAI()

class CustomDataChatbot:
    def __init__(self):
        utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"

    @utils.enable_chat_history
    def main(self):
        st.empty()
        st.sidebar.header(":gift: It's a present for you!")
        st.sidebar.image("background.png", "For Yittbox")
        user_query = st.chat_input(placeholder="Ask me anything!")

        if user_query:
            utils.display_msg(user_query, 'user')

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                stream = client.chat.completions.create(
                    model=self.openai_model,
                    messages=st.session_state.messages,
                    stream=True,
                )
                st.session_state.messages.append({"role": "assistant", "content": ""})
                # print(stream)
                for chunk in stream:
                    chunk_content = chunk.choices[0].delta.content
                    # print(chunk_content)
                    if chunk_content is not None:
                        st.session_state.messages[-1]['content'] += chunk_content
                        message_placeholder.markdown(st.session_state.messages[-1]['content'])
                        


if __name__ == "__main__":
    obj = CustomDataChatbot()
    obj.main()