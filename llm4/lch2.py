from langchain.model_laboratory import ModelLaboratory

from MyLCH import getOpenAI, getGenAI

if __name__=='__main__':
    openllm = getOpenAI()
    genllm = getGenAI()

    model_lab = ModelLaboratory.from_llms([openllm,genllm])
    model_lab.compare("영화 비긴어게인에 대해 한국어로 설명해줘")
