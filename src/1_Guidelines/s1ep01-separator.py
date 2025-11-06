import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 需要 model 总结的内容
target_text = """
你应该提供尽可能清晰、具体的指示，以表达你希望模型执行的任务。\
这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
不要将写清晰的提示与写简短的提示混淆。\
在许多情况下，更长的提示可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
"""
# 提示词模板
user_prompt = """
把用尖括号括起来的文本总结成一句话: <{text}>
"""

model = ChatOpenAI()

# 1. 创建一个提示词模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", user_prompt),
])

# 2. 调用提示词模板
prompt = prompt_template.invoke(input = {"text": target_text})

# 3. 调用模型
response = model.invoke(prompt)

# 4. 打印响应
print(f"[response]\n{response.content}")
