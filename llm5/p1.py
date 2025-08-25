
import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools

from MyLCH import getOpenAI, getGenAI, progressBar
from MyLCH import makeAudio


st.markdown("Page1")
st.sidebar.markdown("Clicked Page1")

text = st.text_area(label="질문입력:",
                    placeholder="질문을 입력 하세요")
if st.button("SEND"):
    if text:
        st.info(text)
        makeAudio(text,"temp.mp3")
        st.audio("audio/temp.mp3",autoplay=True)
        openllm = getOpenAI()
        tools = load_tools(['wikipedia', 'llm-math'], llm=openllm)
        agent = initialize_agent(
            tools,
            openllm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
        my_bar = progressBar("Operation in progress. Please wait.")
        result=agent.run(text)
        st.info(result)
        makeAudio(result, "temp.mp3")
        st.audio("audio/temp.mp3", autoplay=True)
        my_bar.empty()

    else:
        st.info("질문을 입력하세요")

