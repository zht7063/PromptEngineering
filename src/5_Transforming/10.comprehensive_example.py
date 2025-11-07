import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic.deprecated.tools import T
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI()

text = """
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""

prompt_content = """
针对以下三个反引号之间的英文评论文本，进行指定工作：

1. 首先进行拼写及语法纠错，
2. 然后将其转化成中文，
3. 再将其转化成优质淘宝评论的风格，从各种角度出发，分别说明产品的优点与缺点，并进行总结。
4. 润色一下描述，使评论更具有吸引力。

输出结果格式为：
    【优点】xxx
    【缺点】xxx
    【总结】xxx

⭐注意，只需填写xxx部分，并分段输出。将结果输出成Markdown格式。

下面是你要处理的文本：
```{text}```
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
prompt = prompt_template.invoke(input = {"text" : text})

response = model.invoke(prompt);
print(response.content)
