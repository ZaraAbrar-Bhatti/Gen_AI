import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

Google_Chat_Model = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY")
    )

response = Google_Chat_Model.invoke("What is meant by search engine?")

print(response.content)
