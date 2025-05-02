from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

# text = "What is your name?"
# vector = embeddings.embed_query(text)

doc = [
    "What is your name ?",
    "In which class do you read ?",
    "Where do you live ?",
    "What is your gender ?",
    "What is your blood group ?"
]

vector = embeddings.embed_documents(doc)

print(str(vector))