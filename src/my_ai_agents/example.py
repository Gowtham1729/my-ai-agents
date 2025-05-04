from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
from my_ai_agents import models


# model_client = models.get_openai_model_client(
#     model="gpt-4.1-nano-2025-04-14",
# )
model_client = models.get_gemini_model_client(
    model="gemini-2.5-flash-preview-04-17",
)
# model_client = models.get_local_model_client(
#     model="qwen3-30b-a3b",
# )


# Define a simple function tool that the agent can use.
# For this example, we use a fake weather tool for demonstration purposes.
async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"The weather in {city} is 73 degrees and Sunny."


# Define an AssistantAgent with the model, tool, system message, and reflection enabled.
# The system message instructs the agent via natural language.
agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message="You are a helpful assistant.",
    reflect_on_tool_use=True,
    model_client_stream=True,
)


async def main() -> None:
    await Console(agent.run_stream(task="What is the weather in New York?"))
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
