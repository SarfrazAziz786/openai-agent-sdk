from openai_agent_sdk.gemini_config import config
from agents import Agent, Runner , handoff, enable_verbose_stdout_logging
from my_run_hooks import MyRunHooks
from pydantic import BaseModel
from openai_agent_sdk.my_tool import plus

# enable_verbose_stdout_logging()

# class math_output(BaseModel) :
#     result : str





math_assistant = Agent(
    name="math teacher",
    instructions=  """You are a helpful math teacher.
    For every addition question, you MUST call the plus tool.
    Always return in the format: a + b = result""",
    handoff_description="this is a good math assistant",
    tools=[plus],
    
    # output_type=math_output,
)
assistant = Agent(
    name="Assistant",
    instructions="you are helpful assistant",
    handoffs=[handoff(math_assistant)]
)


res = Runner.run_sync(
    starting_agent=assistant,
    input="5+2=?",
    run_config= config,
    hooks=MyRunHooks(),
      

)

print(res.final_output)