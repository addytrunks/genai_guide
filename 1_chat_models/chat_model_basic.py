# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Automatically load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model (automatically infers the API key from the environment)
model = ChatOpenAI(
    model="gpt-4o-mini",
    # Set the temperature to 0 to get deterministic results
    # Set the temperature to 1.0 to get more creative results
    temperature=0,
)

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")

print("Full result:")
print(result)

print("Content only:")
print(result.content)
