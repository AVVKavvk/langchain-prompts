from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

model = ChatDeepSeek(model="deepseek-chat",max_tokens=100)

st.header("Assistant Chatbot")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt("prompt.json")

# prompt = template.invoke({
#   "paper_input": paper_input,
#   "style_input": style_input,
#   "length_input": length_input
# })

if st.button("Summarize"):
  chain = template | model #chain
  result = chain.invoke({
  "paper_input": paper_input,
  "style_input": style_input,
  "length_input": length_input
})
  st.write(result.content)
