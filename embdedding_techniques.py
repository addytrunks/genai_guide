import os
from dotenv import load_dotenv 
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

text = "What is the capital of the moon?"

openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
query_result = openai_embeddings.embed_query(text)
print(len(query_result))


os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
huggingface_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
query_result = huggingface_embeddings.embed_query(text)
print(len(query_result))

