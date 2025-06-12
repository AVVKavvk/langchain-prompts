from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv()

llm = ChatDeepSeek(model="deepseek-chat",max_tokens=100)

result = llm.invoke("Hello, how are you?")
print(str(result))