from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# System Message => Sets the context for the conversation, usually the first message (convention)
# Human Message => The user's message
messages = [SystemMessage(content="You are a math tutor. You are to answer math questions with steps."),
            HumanMessage(content="What is 81 divided by 9?")
            ]

result = model.invoke(messages)
print("Answer from AI: {}".format(result.content))

# AI Message => The AI's response
# Including AI message will provide context
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]

result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
