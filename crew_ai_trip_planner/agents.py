"""
ULTIMATE GOAL (Expert travel agent):  Create a 7-day itinerary with detailed per-day plans which includes budget,packing suggestions,
clothing to wear, safety tips, and restaurants to try out.

WHAT DO OUR AGENTS WANT TO DO?
    1. City Selection Expert
    2. Local Tour Guide
    3. Budget Analyst

NOTE:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume

"""

from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

class TravelAgents:
    def __init__(self):
        self.OpenAIGPT4Mini = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(
                f"""Expert in travel planning and logistics. 
                I have decades of experience making travel itineraries."""),
            goal=dedent(f"""Create a 7-day itinerary with detailed per-day plans which includes budget,packing 
            suggestions, clothing to wear, safety tips, and restaurants to try out."""),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            llm=self.OpenAIGPT4Mini,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(
                f"""Expert at analyzing travel data to pick ideal destinations."""),
            goal=dedent(
                f"""Select the best cities based on weather, season, prices, and traveler interests."""),
            tools=[SearchTools.search_internet],
            llm=self.OpenAIGPT4Mini,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent(
                f"""Local expert with deep knowledge of the area. You are highly energetic and love to share your 
                knowledge."""),
            goal=dedent(
                f"""Provide detailed and best information on local attractions, restaurants, and activities.Create a 
                7-day itinerary with detailed per-day plans which includes budget,packing suggestions, clothing to 
                wear, safety tips, and restaurants to try out. Make sure to provide links to restaurant's website so 
                that the users can check them out."""),
            tools=[SearchTools.search_internet],
            llm=self.OpenAIGPT4Mini,
        )

    def budget_analyst(self):
        return Agent(
            role="Budget Analyst",
            backstory=dedent(
                f"""Expert in budgeting and finance. You are detail-oriented and have a keen eye for numbers."""),
            goal=dedent(
                f"""Analyze travel expenses and provide cost-saving tips and tricks."""),
            tools=[SearchTools.search_internet, CalculatorTools.calculate],
            llm=self.OpenAIGPT4Mini,
        )
