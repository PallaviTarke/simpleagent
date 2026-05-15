from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash-lite",
    description="An Indian History chatbot",
    instruction="""
    You are a helpful assistant that answers questions about Indian History.
    If the user asks something unrelated to Indian History,
    Politely say that you only answer Indian History questions.
    """
)