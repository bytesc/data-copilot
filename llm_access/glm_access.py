
from langchain.prompts import PromptTemplate
from llm_access import get_api

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from llm_access.call_llm_test import call_llm

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key=get_api.get_api_key_from_file("./llm_access/api_key_glm.txt"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)


if __name__ == "__main__":
    print(call_llm("你好", llm))




