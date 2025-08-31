from agents import Agent , Runner, enable_verbose_stdout_logging, handoff, RunContextWrapper
from openai_agent_sdk.gemini_config import config
from openai_agent_sdk.my_tool import plus, weather
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
from agents.extensions import handoff_filters

# enable_verbose_stdout_logging()






class MyInputData ( BaseModel):
    reason : str   
    # Final_result : str


async def service(ctx:RunContextWrapper, input_data:MyInputData):     #on handsoff function 
    print(ctx.context)
    print(input_data.reason)   #output: I need help with a math problem: 12+2=?
    # print(input_data.Final_result)      #output: "14"     answer from assistant


async def enable(ctx:RunContextWrapper,agent:Agent):
    if ctx.context['age'] >= 18:
        return True
    return False

math_assistant = Agent(
    name= "Math Assistant",
    instructions=f"{RECOMMENDED_PROMPT_PREFIX} you are helpful math assistant",
    tools=[plus],
    handoff_description="this is helpful math assistant",

)

math_teacher= handoff(
    math_assistant,
    tool_name_override="math_teacher",
    tool_description_override="this is helpful math teacher",
    on_handoff=service,      #first run this function then agent useful for data fetch , manupulate, context manupulate, database data , manage logs
    input_type=MyInputData,
    input_filter=handoff_filters.remove_all_tools,   #on handsoff not received tools from assistant agent  
    is_enabled=enable
)




assistant = Agent(
    name= "helpful assistant",
    instructions="you are a helpful assistant. You have a weather tool if user querry related to weather use this tool. If math related querry you must handsoff to math teacher",
    handoffs=[math_teacher],
    tools=[weather]
    
) 




result = Runner.run_sync(
    starting_agent=assistant,
    input="what is the weather in Karachi city? and 12+3=?",
    run_config=config,
    context={"name" : "Sarfraz", "age":15, "role":"teacher"}



)

# print(result.final_output)
# print(result.last_agent.name)
# print(assistant.handoffs)
print(result.final_output)
print(result.last_agent.name)