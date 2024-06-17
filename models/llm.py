import os
import getpass
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_nvidia_ai_endpoints import ChatNVIDIA


load_dotenv()
# chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125")

def initialize_llm(llm_model="mistral"):
    if llm_model == "gpt":
        return ChatOpenAI(model="gpt-3.5-turbo-0125")
    elif llm_model == "mistral":
        return ChatNVIDIA(model="mistralai/mixtral-8x7b-instruct-v0.1")
    elif llm_model == "meta":
        return ChatNVIDIA(model="meta/llama3-70b-instruct")
    else:
        raise TypeError("No llm_model available")

def transcription_model():
    return 
