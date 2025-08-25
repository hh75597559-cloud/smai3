from langchain.agents import load_tools, initialize_agent, AgentType, tools
from numpy.f2py.crackfortran import verbose

from MyLCH import getOpenAI, getGenAI

if __name__=='__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    tools = load_tools(['wikipedia','llm-math'],llm=openllm)

    agent = initialize_agent(
        tools,
        openllm,
        agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True

    )

    txt = "영화 비긴어게인에 대해 한국어로 설명해줘"
    print(agent.run(txt))
