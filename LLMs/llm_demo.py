# pyrefly: ignore [missing-import]
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

resp = llm.invoke("Hello, how are you?")
print(resp)