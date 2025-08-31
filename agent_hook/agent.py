from openai_agent_sdk.gemini_config import config
from openai_agent_sdk.my_tool import plus
from agents import Agent, Runner 
from my_agent_hooks import MyAgentHooks



math_assistant = Agent(
    name="Math Assistant",
    instructions="you are helpful Math Teacher ",
    hooks=MyAgentHooks(),
    tools=[plus],
    handoff_description="i'm a math related question querry"


)
assistant = Agent(
    name="Assistant",
    instructions="you are helpful assistant",
    hooks=MyAgentHooks(),
    handoffs= [math_assistant]
)


res = Runner.run_sync(
    starting_agent=assistant,
    input="2+2=?",
    run_config= config,
    context={"id" : "3"}
)

print(res.final_output)