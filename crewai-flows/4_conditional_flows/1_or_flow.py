from crewai.flow.flow import Flow, listen, or_, start


class OrExampleFlow(Flow):

    @start()
    def start_method(self):
        print("Starting flow")
        return "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        print("Second method")
        return "Hello from the second method"

    # The logger method will be called if either start_method or second_method is executed.
    @listen(or_(start_method, second_method))
    def logger(self, result):
        print(f"Logger: {result}")


flow = OrExampleFlow()
flow.kickoff()
