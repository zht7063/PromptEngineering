import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

prompt_content = """
请告诉我以下文本是什么语种: 
```Combien coûte le lampadaire?```
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke({})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
