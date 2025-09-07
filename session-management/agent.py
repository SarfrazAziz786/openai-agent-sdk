from agents import Agent, Runner, RunContextWrapper, OpenAIChatCompletionsModel, RunConfig, SQLiteSession

from openai import AsyncOpenAI
import os
from dotenv import load_dotenv


#LLM IS A STATELESS


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
    model=model
)




assistant = Agent(
    name= "assistant agent",
    instructions="you are a helpful assistant"
    
    )

while True:     
    prompt=input("Write promt here:  ")
    
    if prompt == "e":
        break

    result = Runner.run_sync(
        starting_agent=assistant,
        input = prompt,
        run_config=config,
        
        

    )


    print(result.final_output)