import asyncio
from openai_agent_sdk.gemini_config import config
from agents.run import AgentRunner, set_default_agent_runner
from agents import Agent, Runner

class CustomAgentRunner(AgentRunner):
    async def run(self, starting_agent, input, run_config=config, **kwargs):
        # Custom preprocessing: routing, load balancing, monitoring
        print(f"CustomAgentRunner.run() ")
        
        # Core parent with custom logic  
        result = await super().run(starting_agent, input, **kwargs)
        

        
        # Custom postprocessing: analytics, state persistence, logging
        return result

set_default_agent_runner(CustomAgentRunner())     #set custom runner as a default runner

    
async def main():
    agent = Agent(
        name="Assistant",
        instructions=  "you only respond in haikus"

    )



    result = await Runner.run(
        agent,
        "Tell me about recursion in programing"
    )


    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())