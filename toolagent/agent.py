from google.adk.agents import Agent
from ddgs import DDGS
import datetime


def get_current_time() -> str:
    """
    Get current time
    """

    return datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def duckduckgo_search(query: str) -> str:
    """
    Search the web using DuckDuckGo
    """

    output = ""

    with DDGS() as ddgs:

        search_results = ddgs.text(
            query,
            max_results=5
        )

        for index, r in enumerate(search_results, start=1):

            output += f"""
Result {index}

Title: {r.get('title')}

Description: {r.get('body')}

URL: {r.get('href')}

"""

    return output


root_agent = Agent(

    name="tool_agent",

    model="gemini-2.5-flash-lite",

    description="Tool agent",

    instruction="""
    You are a helpful assistant.

    Available tools:
    - duckduckgo_search → Search the web
    - get_current_time → Get current time
    """,

    tools=[
        duckduckgo_search,
        get_current_time
    ],
)