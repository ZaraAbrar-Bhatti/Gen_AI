from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st
from model import model

with open(r"C:\Users\admin\Desktop\Gen_AI\Langchain\Prompts\Dynamic-Prompt-UI\styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_dotenv()
template = load_prompt("template.json")
LLM = ChatHuggingFace(llm = model)

st.title("📚 ThesisCraft")
st.markdown("Welcome to **ThesisCraft -a basic Research Tool**! Select any of the given below names to summarize the specific research paper.")

st.sidebar.title("About **ThesisCraft**")
st.sidebar.markdown("""
This is a very basic Research Tool which uses an **Open Source Generative model** to summarize various research papers. 
The response is entirely depend upon the prompt which includes:
- **Name of the paper**
- **Length of the response**
- **Format of the response**

Prompt Engineering (Dynamically) has actually been targeted to generate potential summary!


The work has done by **Zara Abrar** F2021266603.
""")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

if st.button("Summarize"):
    chain = template | LLM
    result = chain.invoke({
    "paper_input": paper_input,
    "length_input": length_input,
    "style_input": style_input
})
    st.text(result.content)

st.markdown("---")
st.markdown("© 2025 Research Tool using Open Source Generative model. All rights reserved.")