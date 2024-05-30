from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate


def call_llm(question, llm):
    prompt = PromptTemplate(template="{question}", input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    ans = llm_chain.invoke(question)
    return ans["text"]
