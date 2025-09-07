from openai_agent_sdk.gemini_config import config
from agents import Agent,Runner
from dataclasses import dataclass
import asyncio

@dataclass
class Mydata:
    t1:int
    reason:str

def weather(city:str):
    return f"today weather in {city} is cloudy"


async def main():

    weather_agent = Agent(
        name="helpful assistant"
        instructions="you are a helpful weather assistant and also provide caution about current weather"
        output_type=Mydata
        tools=[weather]

    )


    result = await Runner.run_streamed(starting_agent=math_agent,input = 5 + 3 = ?,run_config=config):
        async for e in result.str


    
