from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=50)

while True:
  user_input = input("User: ")
  if user_input and user_input.lower() =="exit":
    break
  result = model.invoke(user_input)
  print("AI:" ,result.content)
