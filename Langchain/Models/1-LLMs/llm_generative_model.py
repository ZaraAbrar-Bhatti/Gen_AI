from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

Gen_LLM = OpenAI(model="gpt-3.5-turbo-instruct")

output = Gen_LLM.invoke("What is the capital of Pakistan ?")

print(output)

print("Script executed successfully!")   # log


# input is plian text and output is also plain text