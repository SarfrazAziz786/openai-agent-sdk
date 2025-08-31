from agents import  AgentHooks, RunContextWrapper, TContext , Agent, Tool
from typing import Any
import requests


class MyAgentHooks ( AgentHooks):

    async def on_start(self, context: RunContextWrapper[TContext], agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the running agent is changed to this
        agent."""
        print("my agent :  start agent hook")
        print("Start Agent Name", agent.name)
        print("start context:" ,context.context)
        if isinstance(context.context, dict):
            context.context["name"] = "sarfraz"
        else:
            setattr(context.context, "name", "sarfraz")

        if isinstance(context.context, dict) and "id" in context.context:
            user_id = context.context["id"]
        else:
            user_id = getattr(context.context, "id", None)

            
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        res = requests.get(url)
        result = res.json()

        if isinstance(context.context, dict):
            context.context["obj"] = result
        else:
            setattr(context.context, "obj", result)




    async def on_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        print("my agent :  End agent hook")
        print("End Agent Name", agent.name)
        print("end context:" ,context.context)

        

    async def on_handoff(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        source: Agent,
    ) -> None:
        """Called when the agent is being handed off to. The `source` is the agent that is handing
        off to this agent."""
        print( "my handoff hook ")

    async def on_tool_start(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
    ) -> None:
        """Called before a tool is invoked."""
        print("my tool hook started ")

    async def on_tool_end(
        self,
        context: RunContextWrapper[TContext],
        agent: Agent,
        tool: Tool,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        print("my tool hook End ")
        
