from crewai.flow.flow import Flow, listen, start


class UntructuredExampleFlow(Flow):

    @start()
    def first_method(self):
        print("Starting flow")
        print(f"State before first_method:\n{self.state}")
        self.state["message"] = "Hello from unstructured flow"
        self.state["counter"] = 0

    @listen(first_method)
    def second_method(self):
        print(f"State before second_method:\n{self.state}")
        self.state["message"] += " - updated"
        self.state["counter"] += 1

    @listen(second_method)
    def third_method(self):
        print(f"State before third_method:\n{self.state}")
        self.state["message"] += " - updated again"
        self.state["counter"] += 1

        print(f"State after third_method: {self.state}")


flow = UntructuredExampleFlow()
flow.kickoff()

print(f"Final state:\n{flow.state}")
