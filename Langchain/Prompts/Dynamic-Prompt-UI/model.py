import os
from langchain_huggingface import HuggingFaceEndpoint

model = HuggingFaceEndpoint(
    repo_id = "THUDM/GLM-4-32B-0414",
    task = "conversational",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    temperature=0.5,
)



