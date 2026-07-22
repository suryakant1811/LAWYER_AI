from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model

import os

def get_llm():
    llm = init_chat_model(
        # model="gemini-flash-latest",
        # model_provider="google_genai",
        # google_api_key=os.getenv("GEMINI_API_KEY"),
            model="llama-3.3-70b-versatile",
            model_provider="groq",
            api_key=os.getenv("GROQ_API_KEY"),
    )
    return llm