from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat_template

chat_template = ChatPromptTemplate([
  ("system","You are a helpful customer support expert"),
  MessagesPlaceholder(variable_name="history"),
  ("human","{query}")
])

# load chat_history
chat_history=[]

with open('./chat_history.txt') as f:
  chat_history.extend(f.readlines())

# prompt 
prompt = chat_template.invoke({
  "history": chat_history,
  "query": "What is the status of my refund?"
})

print(prompt)