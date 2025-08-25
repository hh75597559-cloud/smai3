import time

import streamlit as st
from click import prompt


from MyLLM import geminiTxt, geminiModel
from MyLLM import progressBar


# sidebar
st.sidebar.markdown("Clicked Page 4")

# page
st.title("Page 4 번역기")
text = st.text_area(label="질문을 입력:",
                    placeholder="질문을 입력 하세요")
language = st.selectbox("언어를 선택 하세요", ["영어", "중국어", "일본어"])

if st.button("SEND"):
    if text and language:
        st.info(f"선택하신 언어는 : {language}")
        st.info(text)
        my_bar=progressBar("Operation in progress. Please wait.")
        result = geminiTxt(f"{language}으로 다음 질문 번역 해줘 {text}")
        my_bar.empty()
        st.info(result)
    else:
        st.info("질문과 언어를 입력하세요")

