import asyncio
import random
from rich import print
from openai.types.responses import ResponseTextDeltaEvent

from agents import Agent, Runner, OpenAIChatCompletionsModel , RunConfig, RunContextWrapper, function_tool
from openai import AsyncOpenAI
from pydantic import BaseModel
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


# Check if the API key is present; if not, raise an error
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")



client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)
model =OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client,)
    
config = RunConfig(
    model = model,
    tracing_disabled=True,
)


# async def main():
#     agent = Agent(
#         name="Joker",
#         instructions="You are a helpful assistant.",
#         model=model
#     )

#     result = Runner.run_streamed(agent, input="Please tell me 5 jokes.")
#     async for event in result.stream_events():
#         print(event)
#         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#             print(event.data.delta, end="", flush=True)



# asyncio.run(main())



from agents import Agent, ItemHelpers, Runner, function_tool


@function_tool
def how_many_jokes() -> int:
    return random.randint(1, 10)


async def main():
    agent = Agent(
        name="Joker",
        instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
        tools=[how_many_jokes],
        model=model
    )

    result = Runner.run_streamed(
        agent,
        input="Hello",

    )
    print("=== Run starting ===")
    async for event in result.stream_events():
        print(event)

        # We'll ignore the raw responses event deltas
        if event.type == "raw_response_event":
            continue
        elif event.type == "agent_updated_stream_event":
            print(f"Agent updated: {event.new_agent.name}")
            continue
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print("-- Tool was called")
            elif event.item.type == "tool_call_output_item":
                print(f"-- Tool output: {event.item.output}")
            elif event.item.type == "message_output_item":
                print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
                
            else:
                pass  # Ignore other event types





asyncio.run(main())

print("=== Run complete ===")