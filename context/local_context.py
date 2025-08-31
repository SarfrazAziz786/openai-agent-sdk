

from agents import Agent, Runner, OpenAIChatCompletionsModel , RunConfig, RunContextWrapper, function_tool
from openai import AsyncOpenAI
from pydantic import BaseModel
import os
from openai_agent_sdk.gemini_config import model

config = RunConfig(
    model = model,
    tracing_disabled=True,
)



class UserInfo(BaseModel):  
    name: str
    age: int

    def display_user_info(self) -> str:
        return f"User: {self.name}, Age: {self.age}"
    
@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:  
    """Fetch the age of the user. Call this function to get user's age information."""
    return f"The user {wrapper.context.name} is 30 years old"


@function_tool
def add(rapper: RunContextWrapper[UserInfo],a: int, b: int) -> int:
    """Add two numbers."""
    print("content : " , rapper)
    print(rapper.context.name)
    print(rapper.context.age)
    print(rapper.context.display_user_info())
    return a + b


user_info = UserInfo(name="sarfraz", age=30)

agent = Agent(  
    name="Assistant",
    instructions="You are a helpful assistant that provides user information.",
    tools=[fetch_user_age, add],
)
result = Runner.run_sync(  
    starting_agent=agent,
    input="What is the sum of 5 and 10?",
    # context=user_info,
    context=user_info,
    run_config=config
)

print(result.final_output)  

