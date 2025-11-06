import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic.deprecated.tools import T
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 演示文本
text = [ 
    "The girl with the black and white puppies have a ball.",  # The girl has a ball.
    "Yolanda has her notebook.", # ok
    "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
    "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
    "Your going to need you’re notebook.",  # Homonyms
    "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
    "This phrase is to cherck chatGPT for spelling abilitty"  # spelling
]

prompt_content = """
请校对并更正以下文本。注意纠正文本保持原始语种，无需输出原始文本。
如果没有发现错误，直接输出“没有错误”。

例如：
输入：I are happy.
输出：I am happy.

注意，输出的时候不需要为输出内容添加任何引号或者反引号，只要输出内容即可。

下面是你要校对的文本：
输入：{input}
输出：
"""

prompt_template = PromptTemplate.from_template(template = prompt_content)
model = ChatOpenAI()

for (idx, t) in enumerate(text):
    prompt = prompt_template.invoke({"input": t})
    response = model.invoke(prompt)
    print(f"[response_{idx}] {response.content}")
