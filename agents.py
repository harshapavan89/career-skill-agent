
from langchain.agents import create_agent

from prompts import SYSTEM_PROMPT
from tools import search_jobs, skill_demand_tool


agent = create_agent(
    model="google_genai:gemini-2.5-flash",
    tools=[
        skill_demand_tool,
        search_jobs
    ],
    system_prompt=SYSTEM_PROMPT
)