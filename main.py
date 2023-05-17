import os
#llms:large languages model support 大语言模型支持
from langchain.llms import OpenAI


# 设置openai的api key
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

"""
1.use llms to generate text
"""
# llm = OpenAI(temperature = 0.9)
# text = "what are 5 vacation destinations for someone who likes to go skiing?"
# print(llm(text))

"""
2.promt management
promts templates:manage promts for LLMS promt管理
"""
#from langchain.prompts import PromptTemplate
# promt = PromptTemplate(
#     input_variables = ["food","sport"],
#     template = "What are 5 vacation destinations for someone who likes to eat {food} or {sport}."
# )
# print(promt.format(food = "pizza",sport = "skiing"))

"""
3.chains 
chains:combine LLMs and promts in multi-step workflows
不必将提示符输入语言模型，而是将其与语言模型组合在一起，以便在多步工作流中使用
"""
# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain
#
# llm = OpenAI(temperature = 0.9)
# prompt = PromptTemplate(
#     input_variables = ["food","sport"],
#     template = "What are 5 vacation destinations for someone who likes to eat {food} or {sport}."
# )
# chain = LLMChain(llm = llm,prompt = prompt)
# print(chain.run(food = "pizza",sport = "skiing"))

"""
agents:Dynamically call chains based on user input
initial agent with:1.the tools 2.the language model 3.the type of agent we want to use
"""
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
os.environ["SERPAPI_API_KEY"]="e4989e7c47dad0956e748dc44aa3a3818145f9c1a324bf5b73986aede9292cb4"
llm = OpenAI(temperature = 0)
tools = load_tools(["serpapi","llm-math"],llm = llm)
agent = initialize_agent(tools,llm,agebt="zero-shot-react-description",verbose = True)
agent.run("who is the president of the united states?")