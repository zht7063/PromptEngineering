import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

prompt_content = "You are a helpful assistant named {input}"

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke(input = {"input": "John"})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
