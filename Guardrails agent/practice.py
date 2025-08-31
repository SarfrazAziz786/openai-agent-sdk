from agents import Agent , Runner , InputGuardrailTripwireTriggered, GuardrailFunctionOutput,RunContextWrapper, input_guardrail
from openai_agent_sdk.gemini_config import config
from pydantic import BaseModel

class My_Data_Output(BaseModel):
    isSarfrazRelatedQuerry : bool
    reason : str


guardrail_agent= Agent(
    name = "Guardrail Agent",
    instructions="Check Sarfraz Related Querry only",
    output_type=My_Data_Output

)

@input_guardrail
async def input_guardrail_func(ctx:RunContextWrapper, agent:Agent, input):
    result= await Runner.run(starting_agent=guardrail_agent, input=input, run_config=config)
    final_output:My_Data_Output = result.final_output
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not final_output.isSarfrazRelatedQuerry
    )






personal_assistant = Agent(
    name="Sarfraz Assistant",
    instructions="you are a Sarfraz Assistant , only answer about sarfraz related . Sarfraz's father name is Abdul Aziz, he is 30 year old, his qualification is BCOM , he live in Karachi.",
    input_guardrails=[input_guardrail_func]

)




try:
    result = Runner.run_sync(starting_agent=personal_assistant, input="what is the father name of sarfraz",run_config=config)
    print(result.final_output)
except InputGuardrailTripwireTriggered as e:
    print (f"Input Tripwire \n {e}")