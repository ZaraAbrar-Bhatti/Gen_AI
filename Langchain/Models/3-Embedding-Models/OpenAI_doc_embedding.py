from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings( model="text-embedding-3-large", dimensions=32)

document = [
    "Islamabad is the capital of Pakistan.",
    "Dehli is the capital of India.",
    "Paris is the capital of France.",
    "Washington is the capital of United States of America.",
    "Riyadh is the capital of Saudi Arabia.",
    "London is the capital of United Kingdoms.",
    "Abu Dhabi is the capital of Dubai."
]

result = embeddings.embed_documents(document)

print(str(result))