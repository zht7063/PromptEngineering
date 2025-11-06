import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                              # My screen is flashing
]

model = ChatOpenAI()

for message in user_messages:
    prompt_template_check_language = PromptTemplate.from_template(template = "请告诉我以下使用反引号括起来的文本是什么语种: ```{message}```")
    prompt_check_language = prompt_template_check_language.invoke({"message": message})
    response_check_language = model.invoke(prompt_check_language)

    prompt_template_translate = PromptTemplate.from_template(template = """
        请将下面用反引号括起来的内容翻译成中文和英文，

        你的回答的格式应该是：

        中文翻译：（中文翻译内容）
        英文翻译：（英文翻译内容）
        其中，括号不属于输出内容。

        下面是你要翻译的内容：
        ```{message}```
    """)
    prompt_translate = prompt_template_translate.invoke({"message": message})
    response_translate = model.invoke(prompt_translate)
    
    print(f"[response_check_language] {response_check_language.content}")
    print(f"[response_translate] \n{response_translate.content}")
    print("--------------------------------\n")
