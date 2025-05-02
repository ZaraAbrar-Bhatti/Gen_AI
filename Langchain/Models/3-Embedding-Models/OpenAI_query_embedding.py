from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large", 
    dimensions=32  # high no of dimensions means high contextual meaning + high cost
)

result = embeddings.embed_query("Islamabad is the capital of Pakistan.")

print(str(result))
