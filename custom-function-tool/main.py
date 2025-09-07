from openai_agent_sdk.gemini_config import config
from pydantic import BaseModel
from agents import Agent,Runner, FunctionTool, RunContextWrapper
from openai_agent_sdk.my_tool import plus

class MyToolSchema(BaseModel):
    n1 : int
    n2 : int


async def subtract_function(ctx:RunContextWrapper,arg)->str:
    obj = MyToolSchema.model_validate_json(arg) 
    # model_validate_json validates the JSON returned by the LLM against your tool’s schema. If the JSON matches the schema (correct fields and types), it creates a MyToolSchema object; otherwise, it raises a validation error.
    print("------subtract tool fire------")
    return f"Your Answer is {obj.n1-obj.n2}. "

 


subtract=FunctionTool(

    name="subtract_tool",
    description="Substract function",
    params_json_schema=MyToolSchema.model_json_schema(), # it convert my tool schema to json schema 
    on_invoke_tool=subtract_function,
    # is_enabled=False
    

)



assistant = Agent(
    name= "helpful assistant",
    instructions="you are helpful assistant",
    tools=[subtract]
    
) 


result = Runner.run_sync(
    starting_agent=assistant,
    input = "100-5=?",
     run_config=config,
    context={"name" : "Sarfraz", "age":15, "role":"teacher"}
)

# print(assistant.tools)

# for s in assistant.tools:
#     print(s.params_json_schema)

print(result.final_output)