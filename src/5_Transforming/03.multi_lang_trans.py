import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

prompt_content = """
请将以下文本分别翻译成中文、英文、法语和西班牙语: 
```I want to order a basketball.```
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke({})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
