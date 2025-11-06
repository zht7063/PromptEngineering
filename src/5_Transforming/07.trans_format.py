import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt_content = """
将以下反引号括起来的 Python 字典从 JSON 转换为 HTML 表格，保留表格标题和列名。

你的输出将会是一段可以直接在浏览器中显示的 HTML 代码，不需要有任何前缀、后缀，或者其他内容。

下面是你要转换的 Python 字典：
```{data_json}```
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke({"data_json": data_json})

model = ChatOpenAI()
response = model.invoke(prompt)
# 在同名 ipynb 中可以显示 html 内容。
print(f"[response] \n{response.content}")
