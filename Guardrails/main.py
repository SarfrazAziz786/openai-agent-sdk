from pydantic import BaseModel
from agents import  Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, RunContextWrapper, Runner, TResponseInputItem, input_guardrail, OpenAIChatCompletionsModel, RunConfig, output_guardrail
from openai import AsyncOpenAI
from pydantic import BaseModel
import os
import asyncio

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model=OpenAIChatCompletionsModel(
        model="gemini-1.5-flash",
        openai_client=client,
    )

config = RunConfig(
    model=model,
    tracing_disabled=True,
)


class MathHomeworkOutput(BaseModel):
    is_math_homework: bool
    reasoning: str

class CountryOutput(BaseModel):
    is_country_allowed: bool
    reasoning: str
    country : str
    capital: str
    answer: str

country_guardrail_agent = Agent(
    name="Country guardrail check",
    instructions="we only allow to talk about Pakistan. Don't answer questions about any other.",
    output_type=CountryOutput,
    model=model
)  

@output_guardrail
async def guardrail_output(
    ctx: RunContextWrapper, agent: Agent, output: CountryOutput
) -> GuardrailFunctionOutput:
    
    result = await Runner.run(country_guardrail_agent, output.answer, context=ctx.context)
    print("\n\n Guardrail function is executed , result:", result.final_output, "\n\n")
    
    return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=result.final_output.is_country_allowed is False,
        )
    
    raise GuardrailTripwireTriggered(
        message="Country guardrail triggered",
        output_info=result.final_output,
    )


math_guardrail_agent = Agent( 
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
)


@input_guardrail
async def math_guardrail( 
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    result = await Runner.run(math_guardrail_agent, input, context=ctx.context , run_config=config)
    
    print("\n\n Guardrail function is executed , result:", result.final_output, "\n\n")

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=result.final_output.is_math_homework,
    )


agent = Agent(  
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail],
    output_guardrails=[])



async def main():
    # This should trip the guardrail
    try:
        # result = await Runner.run(agent, "Hello, can you help me solve for x: 2x + 3 = 11?" , run_config=config)
        result = await Runner.run(agent, "Who was the founder of Pakistan ?" , run_config=config)
        print(result.final_output.model_dump())
        print("Guardrail didn't trip - this is unexpected")

    except InputGuardrailTripwireTriggered:
        print("Math homework guardrail tripped")

if __name__ == "__main__":
    asyncio.run(main())