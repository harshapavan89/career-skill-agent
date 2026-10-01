import streamlit as st

from agents import agent

st.set_page_config(
    page_title="SkillMap Agent",
    page_icon="🚀"
)

st.title("🚀 SkillMap AI Agent")

query = st.text_input(
    "Enter a skill",
    placeholder="Generative AI"
)

location = st.text_input(
    "Location",
    value="India"
)

if st.button("Analyze Skill"):

    with st.spinner("Researching..."):

        user_query = f"""
        What's the demand for {query}
        in the industry and show
        related job openings in {location}
        """

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
            }
        )

        final_response = result["messages"][-1].content

        if isinstance(final_response, list):
             final_response = final_response[0]["text"]

        st.markdown(final_response)