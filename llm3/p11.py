import time

import streamlit as st
from PIL import Image
from openai import images

from MyLLM import geminiTxt, progressBar, save_uploadedfile
from MyLLM import makeimg

# Sidebar
st.sidebar.markdown("Clicked Page 11")

# Page
st.title("Page 11")
text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
name=st.text_input(label="이미지 이름:",
                   placeholder="이미지 이름을 입력 하세요")
if st.button("SEND"):
    if text and name:
        st.info(text)
        makeimg(text, name)
        with open("img/"+name,"rb") as file:
            st.download_button(
                label="Download image",
                data=file,
                file_name="img/"+name,
                mime="image/png"
        )
        img = Image.open("img/"+name)
        st.image(img)
    else:
        st.info("다시 입력하세요")

