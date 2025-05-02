from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodel = ChatOpenAI(model = "gpt-3.5-turbo")

response = chatmodel.invoke("Tell me a Programming joke...")

print(response)

print("Script executed successfully!")   #log

# Input is plain text but output is not. ALong with original output string it contains multiple parameters also (metadata).

print(response.content)

print("Script executed successfully!")

# So if you want only desired string (plain text) in your output, fetch the specific object which holds it!




