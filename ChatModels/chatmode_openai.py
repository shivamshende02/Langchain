# pyrefly: ignore [missing-import]
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-4",temperature=0)

resp = chat.invoke("Hello, how are you?")
print(resp)
