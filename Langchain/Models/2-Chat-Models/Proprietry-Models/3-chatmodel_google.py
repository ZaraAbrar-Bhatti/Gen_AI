from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

Google_Chat_Model = ChatGoogleGenerativeAI(model = "Gemini 1.5 Pro")

response = Google_Chat_Model.invoke("What is meant by search engine?")

print(response.content)
