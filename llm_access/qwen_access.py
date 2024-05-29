from langchain_community.llms import Tongyi
# pip install -U langchain-community
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# pip install dashscope

from llm_access import get_api

model = "qwen-turbo"
llm = Tongyi(dashscope_api_key=get_api.get_api_key_from_file(),
             model_name=model)

# path = r'D:\IDLE\big\qwen\models\Qwen-1_8B-Chat'
# from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
# from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
# # pip install tiktoken torch
# # pip install transformers_stream_generator einops
# # pip install accelerate
# tokenizer = AutoTokenizer.from_pretrained(path, revision='master', trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained(path, revision='master', device_map="auto", trust_remote_code=True)
# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10)
# llm = HuggingFacePipeline(pipeline=pipe)


if __name__ == "__main__":
    prompt = PromptTemplate(template=" ", input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    ans = llm_chain.invoke("你好")
    print(ans)
