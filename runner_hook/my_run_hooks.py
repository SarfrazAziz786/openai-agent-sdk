from agents import RunHooks, RunContextWrapper,Agent, Tool
from typing import Any

class MyRunHooks (RunHooks):

    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
    
        """Called before the agent is invoked. Called each time the current agent changes."""
        print("my start run hook")
        print("Agent Name : " , agent.name)

    async def on_agent_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        print("my end run hook")
        print("Agent Name : " , agent.name)

    async def on_handoff(
        self,
        context: RunContextWrapper,
        from_agent: Agent,
        to_agent: Agent,
    ) -> None:
        """Called when a handoff occurs."""
        print("run hook handoff")
        print(f"from agent name: {from_agent.name} and to agent name : {to_agent.name}")

    async def on_tool_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Called before a tool is invoked."""
        print("start tool run hook ")
        print("tool parameter--->", tool)

    async def on_tool_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        print("End tool run hook ")
        
