"""
Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itinerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analyze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.
    - Budget Analyst : Analyze the budget and provide recommendations.

Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**:
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)
"""

from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, you'll be rewarded."

    def plan_itinerary(self, agent, city, travel_dates, interests, budget):
        self.task = Task(description=dedent(f"""
                **Task**: Develop a 7-Day Travel Itinerary
                **Description**: Expand the city guide into a full 7-day travel itinerary with detailed 
                    per-day plans, including weather forecasts, places to eat, packing suggestions, 
                    and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, 
                    and actual restaurants to go to. This itinerary should cover all aspects of the trip, 
                    from arrival to departure, integrating the city guide information with practical travel logistics.

                **Parameters**: 
                - City: {city}
                - Trip Date: {travel_dates}
                - Traveler Interests: {interests}
                - Budget: {budget}

                **Note**: {self.__tip_section()}
            """), agent=agent,
                         expected_output="A comprehensive 7-day itinerary including places to visit, stay, eat, and budget breakdown.")
        return self.task

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Identify the Best City for the Trip
                    **Description**: Analyze and select the best city for the trip based on specific 
                        criteria such as weather patterns, seasonal events, and travel costs. 
                        This task involves comparing multiple cities, considering factors like current weather 
                        conditions, upcoming cultural or seasonal events, and overall travel expenses. 
                        Your final answer must be a detailed report on the chosen city, 
                        including actual flight costs, weather forecast, and attractions.

                    **Parameters**: 
                    - Origin: {origin}
                    - Cities: {cities}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output="A detailed report on the selected city, including flight costs, weather forecast, "
                            "and attractions."
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city, gathering information about 
                        key attractions, local customs, special events, and daily activity recommendations. 
                        This guide should provide a thorough overview of what the city has to offer, including 
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.
                        You must provide the final result ONLY in markdown format or you will be severely penalized.

                    **Parameters**: 
                    - City: {city}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output="A comprehensive city guide with attractions, customs, events, and recommendations."
        )

    def prepare_budget_plan(self, agent, budget, travel_dates):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Develop a Detailed Budget Plan
                    **Description**: Create a detailed budget plan for the trip, including estimated costs 
                        for flights, accommodations, meals, transportation, activities, and miscellaneous expenses. 
                        This plan should be comprehensive, realistic, and tailored to the traveler's preferences and 
                        financial constraints. Provide a breakdown of expenses for each day of the trip, 
                        considering all possible costs and contingencies.

                    **Parameters**: 
                    - Budget: {budget}
                    - Travel Date: {travel_dates}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output="A detailed budget plan with daily expense breakdowns and contingency planning."
        )
