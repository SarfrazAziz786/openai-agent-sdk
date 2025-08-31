from agents import Agent, Runner, set_tracing_export_api_key,OpenAIChatCompletionsModel, RunConfig, ModelSettings, enable_verbose_stdout_logging, trace
from openai import AsyncOpenAI
from openai_agent_sdk.my_tool import plus,Subtract,multiply
from decouple import config
import os
from dotenv import load_dotenv
load_dotenv() 
from rich import print

enable_verbose_stdout_logging()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


external_client = AsyncOpenAI (
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai")

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
    )

gemini_config = RunConfig(    
    model=model
)





# CONFIRATION USING TRACING BY OPENAI KEY WITH LLM MODEL OF GEMINI

OPENAI_KEY = config("OPENAI_API_KEY", default="your default openai key") 

if not isinstance(OPENAI_KEY, str):
    raise ValueError("OPENAI_API_KEY must be a string.")


set_tracing_export_api_key(OPENAI_KEY)








math_agent = Agent(
    name="math_assistant",
    instructions="You are a helpful assistant.For any math problem, always use the tool.",
    handoff_description="math related querry and provide solution",
    tools=[plus,Subtract,multiply],
    model=model
)

english_agent = Agent(
    name="english_Assistant",
    instructions="You are a helpful assistant.For any english problem like translate , essay writing.",
    handoff_description="english related querry and provide solution",
    model=model
)




assistant_agent = Agent(
    name="orchestrator_agent",
    instructions="You are a helpful assistant.",
    # tools=[math_agent.as_tool(tool_name="math_tool", tool_description="math related querry solution"),
    #        english_agent.as_tool(tool_name="english_tool", tool_description="english related querry solution")],
    )




with trace("My test workflow"):

    result1 = Runner.run_sync(
        starting_agent=assistant_agent,
        input="5+3",
        run_config=gemini_config,
        
        )
    
    result2 = Runner.run_sync(
        starting_agent=assistant_agent,
        input=f"{result1.final_output} * 1000",
        run_config=gemini_config,
        
        )
    
    



    print(result2.final_output)
    # print(result.last_agent)