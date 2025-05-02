from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

Anthropic_Chat_Model = ChatAnthropic(model= "Claude 3 Opus")

response = Anthropic_Chat_Model.invoke("Tell some programming related joke...")

print(response.content)