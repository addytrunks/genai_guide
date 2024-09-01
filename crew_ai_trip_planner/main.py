from crewai import Crew
from dotenv import load_dotenv

from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
import streamlit as st

load_dotenv()


class TripCrew:
    def __init__(self, origin, cities, date_range, interests, budget):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests
        self.budget = budget

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define your custom agents and tasks here
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()
        budget_analyst = agents.budget_analyst()

        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests,
            self.budget
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests,
        )

        budget_analysis = tasks.prepare_budget_plan(
            budget_analyst,
            self.cities,
            self.date_range,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, budget_analyst, local_tour_guide],
            tasks=[plan_itinerary, identify_city, budget_analysis, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# Function to validate user input
def validate_inputs(origin, cities, date_range, interests, budget):
    if not origin or not cities or not date_range or not interests or not budget:
        st.error("Please fill out all the fields to plan your trip")
        return False
    return True


if __name__ == "__main__":

    # Display headers and input fields
    st.header("Welcome to Trip Planner Crew")
    st.subheader('Please fill out the following information to plan your trip')
    st.divider()

    origin = st.sidebar.text_input("From where will you be traveling from?", placeholder='City, Country')
    cities = st.sidebar.text_input("What are the cities options you are interested in visiting?",
                                   placeholder='City1, City2, City3')
    date_range = st.sidebar.text_input("What is the date range you are interested in traveling?",
                                       placeholder='Month-Month, Year')
    interests = st.sidebar.text_input("What are some of your high-level interests and hobbies?",
                                      placeholder='Hiking, Beach, Shopping, etc.')
    budget = st.sidebar.text_input("What is your budget for this trip?", placeholder='$5000')

    # Initialize trip planning flag
    generating_result = False

    if generating_result:
        st.write("Trip Planning........")

    # Validate inputs before planning the trip
    if st.sidebar.button("Plan Trip"):
        if validate_inputs(origin, cities, date_range, interests, budget):
            trip_crew = TripCrew(origin, cities, date_range, interests, budget)
            generating_result = True
            result = trip_crew.run()
            st.markdown(result)
            generating_result = False
