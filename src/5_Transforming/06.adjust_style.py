import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

prompt_content = """
将以下用反引号括起来的文本翻译成商务信函的格式: 
```小老弟，我小羊，上回你说咱部门要采购的显示器是多少寸来着？```
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke({})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
