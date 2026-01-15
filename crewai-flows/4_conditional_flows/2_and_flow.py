from crewai.flow.flow import Flow, and_, listen, start


class AndExampleFlow(Flow):

    @start()
    def start_method(self):
        print("---- Start Method ----")
        self.state["greeting"] = "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        print("---- Second Method ----")
        self.state["joke"] = "What do computers eat? Microchips."

    @listen(and_(start_method, second_method))
    def logger(self):
        print("---- Logger ----")
        print(self.state)


flow = AndExampleFlow()
flow.kickoff()
