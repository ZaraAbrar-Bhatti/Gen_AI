from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

chatLLM = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs=dict(
        do_sample = True,
        temperature = 0.5,
        max_new_tokens = 200
    )
)

chatmodel = ChatHuggingFace(llm = chatLLM)
response = chatmodel.invoke("Who is Quaid e Azam Muhammad Ali Jinnah?")

print(response.content)



