from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
 [
  ("system","You are a helpful {domain} expert"),
  ("user","I have a question about {topic}"),
 ]
)

prompt = chat_template.invoke({
  "domain": "Mathematics",
  "topic": "Trigonometry"})

print(prompt)