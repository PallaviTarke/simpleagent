import os
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents import LlmAgent

model = LiteLlm(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
)

def get_weather(city: str):
    return f"The weather in {city} is 30°C and sunny."

root_agent = LlmAgent(
    name="weather_agent",
    model=model,
    description="Weather assistant",
    instruction="""
    You are a weather assistant.
    Always use the tool `get_weather` to answer weather questions.
    """,
    tools=[get_weather],
)