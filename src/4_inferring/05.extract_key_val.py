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
从评论文本中识别以下项目：
- 评论者购买的物品
- 制造该物品的公司

评论文本用三个反引号分隔。将你的响应格式化为以 "item" 和 "brand" 为键的 toml 对象。
如果信息不存在，请使用 "unknown" 作为值。
让你的回应尽可能简短。
  
评论文本: ```{lamp_review_zh}```
"""

prompt_template = PromptTemplate(template = template_content)
prompt = prompt_template.invoke(input = {"lamp_review_zh": lamp_review_zh})

model = ChatOpenAI()
response = model.invoke(prompt)
print(f"[response] \n{response.content}")
