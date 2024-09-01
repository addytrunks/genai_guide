from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Set an initial system message (optional)
chat_history = [SystemMessage(content="You are a helpful assistant,respond to user queries as polite as possible.")]

print("You can start chatting with the bot now.\n")

while True:
    user_query = input("Ask any questions (Enter N/n to exit the chat):")

    if user_query.lower() == 'n':
        break
    else:
        chat_history.append(HumanMessage(content=user_query.lower()))

        result = model.invoke(chat_history)
        print("AI Response:", result.content)

        chat_history.append(AIMessage(content=result.content))

print("\nThank you for using the application")

print("\n\n---- Message History ----")
print(chat_history)
