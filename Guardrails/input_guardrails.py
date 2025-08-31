
from agents import (Agent, Runner, OpenAIChatCompletionsModel ,
                     RunConfig, function_tool, 
                     input_guardrail, TResponseInputItem, RunContextWrapper ,GuardrailFunctionOutput )
from openai import AsyncOpenAI
from pydantic import BaseModel
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

config = RunConfig(
    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=client,
    ),
    tracing_disabled=True,


)

@input_guardrail   #two ways to guardrail an agent, one is to use the decorator .
async def my_guardrail( 
    ctx: RunContextWrapper, 
    agent: Agent, 
    input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    print("Guardrail function is excuted")

    # result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=None, 
        tripwire_triggered=True,
    )


agent = Agent(  
    name="Assistant",
    instructions="You are a helpful assistant",
    input_guardrails = [my_guardrail],  # add the guardrail to the agent
)

result = Runner.run_sync(  
    starting_agent=agent,
    input = "what is the capital of pakistan?",
    run_config=config
)

print(result.final_output)
# print(result.input_guardrail_results)



