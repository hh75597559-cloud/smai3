import time

import streamlit as st

from MyLLM import makeAudio, progressBar, makeMsg, openAiModelArg

# Sidebar
st.sidebar.markdown("Clicked Page 8")

# Page
st.title("Page 8")
system = st.text_input("SYSTEM", placeholder="system 을 입력")
text=st.text_input("질문 입력",placeholder="질문을 입력하세요")
if st.button("SEND"):
        if system and text:
            makeAudio(text, "temp.mp3")
            st.audio("audio/temp.mp3", autoplay=True)
            st.info(f"{system}에게 {text}을 문의 합니다")
            msg = makeMsg(system, text)
            my_bar = progressBar("Operation in progress. Please wait.")
            result = openAiModelArg("gpt-4o", msg)
            my_bar.empty()
            st.info(result)
            makeAudio(result, "result.mp3")
            st.audio("audio/result.mp3", autoplay=True, width=1)
        else:
            st.audio("audio/retry.mp3", autoplay=True, width=1)
            st.info("입력하세요")
