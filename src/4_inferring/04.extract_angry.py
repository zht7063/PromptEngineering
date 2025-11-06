import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

lamp_review_zh = """
我需要一盏漂亮的卧室灯，这款灯具有额外的储物功能，价格也不算太高。\
我很快就收到了它。在运输过程中，我们的灯绳断了，但是公司很乐意寄送了一个新的。\
几天后就收到了。这款灯很容易组装。我发现少了一个零件，于是联系了他们的客服，他们很快就给我寄来了缺失的零件！\
在我看来，Lumina 是一家非常关心顾客和产品的优秀公司！
"""

template_content = """
接下来用三个反引号标记了一个商品的评论，你的任务是检查评论的内容，判断评论的作者是否表达了愤怒的情绪？

你需要给出是或者否的答案，答案的格式为：是或者否，不需要其他内容。

评论文本: ```{lamp_review_zh}```
"""

prompt_template = PromptTemplate(template = template_content)
prompt = prompt_template.invoke(input = {"lamp_review_zh": lamp_review_zh})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
