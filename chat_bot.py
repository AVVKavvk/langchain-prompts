from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=50)
history=[
  SystemMessage(content="You are a helpful assistant.")
]

while True:
  user_input = input("User: ")
  history.append(HumanMessage(content=user_input))
  if user_input and user_input.lower() =="exit":
    break
  result = model.invoke(history)
  history.append(AIMessage(content=result.content))
  print("AI:" ,result.content)

print(history)
