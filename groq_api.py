import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
parser = StrOutputParser()

# Method 1
messages = [
    SystemMessage(content="Translate the following from English to Spanish.NO PREAMBLE!"),
    HumanMessage(content="Hello How are you?")
]

response = model.invoke(messages)
print(parser.invoke(response))

# Method 2
chain = model|parser
print(chain.invoke(messages))