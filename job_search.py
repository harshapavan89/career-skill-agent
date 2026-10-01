import requests
import streamlit as st

def search_jobs(skill: str, location: str) -> list:

    url = "https://jsearch.p.rapidapi.com/search-v2"

    querystring = {
        "query": f"{skill} jobs in {location}",
        "country": "in",
        "num_pages": "1"
    }

    headers = {
        "x-rapidapi-key": st.secrets.get("RAPID_API_KEY"),
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    data = response.json()

    jobs = data.get("data", [])
    job_list = []

    for job in jobs:

        job_info = {
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "url": job.get("job_apply_link"),
            "job_apply_link": job.get("job_apply_link")
        }

        job_list.append(job_info)

    return job_list

