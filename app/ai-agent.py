class AIAgent:

    def __init__(self, name, model, version):
        self.name = name
        self.model = model
        self.version = version

    def introduce(self):
        print(f"Hello! I am {self.name}.")

    def show_details(self):
        print(f"Name   : {self.name}")
        print(f"Model  : {self.model}")
        print(f"Version: {self.version}")

agent = AIAgent("ResearchBot","gpt-5.5",1.0)
coding_agent = AIAgent("CodeBot", "gpt-5.5", 1.0)
tutor_agent = AIAgent("TutorBot", "gpt-5.5", 1.0)
agent.introduce()
agent.show_details()
coding_agent.introduce()
coding_agent.show_details()
tutor_agent.introduce()
tutor_agent.show_details()
