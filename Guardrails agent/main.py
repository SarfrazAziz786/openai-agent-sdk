from agents import Agent, Runner , RunContextWrapper, GuardrailFunctionOutput, input_guardrail, InputGuardrailTripwireTriggered, output_guardrail, OutputGuardrailTripwireTriggered, TResponseInputItem
from openai_agent_sdk.gemini_config import config, model
from pydantic import BaseModel

class MessageOutput(BaseModel):
    response: str

class MyDataOutput ( BaseModel):
    is_hotel_SRC_querry: bool
    is_hotel_SRC_account_and_tax_querry: bool
    reason: str


guardrail_agent = Agent(
    name= "Guardrail Agent",
    instructions="Check Hotel SRC Queries and account or tax query",
    output_type=MyDataOutput,



)



@input_guardrail
async def guardrail_input_func(ctx:RunContextWrapper[None],agent:Agent , input:str | list[TResponseInputItem])->GuardrailFunctionOutput:
    
    result = await Runner.run(starting_agent=guardrail_agent, input=input, context=ctx.context , run_config=config)
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_SRC_querry
    )





@output_guardrail
async def output_guardrail_func(ctx:RunContextWrapper, agent:Agent, output:MessageOutput )-> GuardrailFunctionOutput:
    result= await Runner.run(starting_agent=guardrail_agent, input=output.response, context=ctx.context, run_config=config)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_hotel_SRC_account_and_tax_querry
    )












hotel_assistant = Agent(
    name= "Hotel Customer Care Assistant",
    instructions="""
    you are a helpful hotel SRC customer care assistant , your name is Ahmed,
    - Hotel SRC owner name is Sarfraz.
    -Hotel total rooms  200.
    -20 rooms for not available for public it only special guest.
    """,
    model=model,
    input_guardrails=[guardrail_input_func],
    output_guardrails=[output_guardrail_func]

)

try:
    result = Runner.run_sync(
    starting_agent=hotel_assistant,
    input= "who is the owner of SRC hotel and how much tax SRC hotel paid in last year",
    run_config=config
)
    print(result.final_output)
    
except InputGuardrailTripwireTriggered as e:
    print(f"Trip Input \n {e}")

except OutputGuardrailTripwireTriggered as e:
    print(f"Trip output \n {e}")







