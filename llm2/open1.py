from myllm.Myapi import makeMsg, openAiModelArg


def test(prompt):
    modelName = "gpt-4o"
    msg = makeMsg("너는 친절한 한국어 선생님",prompt)
    result = openAiModelArg(modelName, msg)
    print(result)

if __name__ == '__main__':
    prompt = "닌텐도스위치2에 대해 2줄로 알려줘"
    test(prompt)