from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
load_dotenv() 

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


external_client = AsyncOpenAI (
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai")

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
    )

config = RunConfig(
    tracing_disabled=True,
    
    model=model
)
