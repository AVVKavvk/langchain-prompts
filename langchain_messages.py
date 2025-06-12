from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=100)

message = [
  SystemMessage(content="You are a helpful assistant."),
  HumanMessage(content="Tell me about langchain"),
]

result = model.invoke(message)
message.append(AIMessage(content=result.content))
print(message)