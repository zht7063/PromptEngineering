import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

input = "John"

template_content = "You are a helpful assistant named {input}"

prompt_template = PromptTemplate(template = template_content)
prompt = prompt_template.invoke(input = {"input": input})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
