

import requests
from langchain.tools import tool
from langchain_tavily import TavilySearch

import streamlit as st
# ---------------------------
# Skill Demand Tool
# ---------------------------

skill_demand_tool = TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=st.secrets["TAVILY_API_KEY"]
)


# ---------------------------
# Job Search Tool
# ---------------------------

@tool
def search_jobs(skill: str, location: str) -> list:
    """
    Search for jobs requiring a specific skill
    in a given location using JSearch API.
    """

    

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "x-rapidapi-key": st.secrets["RAPID_API_KEY"],
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    querystring = {
        "query": f"{skill} jobs in {location}",
        "page": "1",
        "num_pages": "1",
        "country": "in"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    data = response.json()

    jobs = []

    for job in data.get("data", [])[:10]:

        jobs.append(
            {
                "title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_city"),
                "employment_type": job.get("job_employment_type"),
                "apply_link": job.get("job_apply_link")
            }
        )

    return jobs