from openai_agent_sdk.gemini_config import config
from agents import Agent, Runner, enable_verbose_stdout_logging, handoff, set_tracing_disabled, ModelSettings
from openai_agent_sdk.my_tool import plus, multiply, Subtract
import asyncio

enable_verbose_stdout_logging()

math_agent = Agent(
    name="Math Teacher",
    instructions="you are a math teacher. Use this agent for solving mathematical problems, including addition, subtraction, multiplication, and explaining solutions in a clear  ",
    handoff_description="Use this agent for solving mathematical problems, including addition, "
                        "subtraction, multiplication, and explaining solutions in a clear, "
                        "step-by-step manner like a teacher.",
    tools=[plus, multiply, Subtract]

)


assistant_agent = Agent(
    name="helpful_assistant",
    instructions="You are a helpful assistant.For any math problem, always use the math_teacher_tool.",
    tools=[
        math_agent.as_tool(
            tool_name="math_teacher_tool",
            tool_description="this is a math teacher tool."
        )
    ]
)

async def main():
    result = await Runner.run(
        starting_agent=assistant_agent,
        input="please provide the answer : 5 + 3",
        run_config=config,
        )

    print(result.final_output)
    print(result.last_agent.name)
    
asyncio.run(main())