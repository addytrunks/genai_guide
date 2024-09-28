from dotenv import load_dotenv 
from langchain_openai import OpenAIEmbeddings

load_dotenv()

openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

text = "What is the capital of the moon?"
query_result = openai_embeddings.embed_query(text)


