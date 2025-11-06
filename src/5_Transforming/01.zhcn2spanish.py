import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

prompt_content = """
将以下反引号括起来的中文翻译成西班牙语:
```您好，我想订购一个搅拌机。```
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke({})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
