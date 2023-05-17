import os
#llms:large languages model support 大语言模型支持
from langchain.llms import OpenAI
#promts templates:manage promts for LLMS promt管理
from langchain.prompts import PromptTemplate

# 设置openai的api key
os.environ['OPENAI_API_KEY'] = "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"
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

llm = OpenAI(temperature = 0.9)

text = "what are 5 vacation destinations for someone who likes to go skiing?"
print(llm(text))
