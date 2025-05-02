from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "My name is Zara Abrar.",
    "I am an undergraduate of BSCS at UMT.",
    "I live in Lahore Pakistan.",
    "I am female.",
    "I don't know about my blood group."
]

query = "What is your gender?"

doc_embeddings = embeddings.embed_documents(documents)  # a 2D list
query_embeddings = embeddings.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings) #take both arguments as 2D lists
scores = np.array(scores).flatten()

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print ("Query: ", query)
print("Matched response: ", documents[index])
print("The similarity score is = ", score)




