class AIAgent:

    def __init__(self, name, model, version):
        self.name = name
        self.model = model
        self.version = version

    def introduce(self):
        print(f"Hello! I am {self.name}, running on {self.model} (Version {self.version}).")

    def show_details(self):
        print("=" * 30)
        print(f"Name   : {self.name}")
        print(f"Model  : {self.model}")
        print(f"Version: {self.version}")

    def update_model(self, new_model):
        self.model = new_model

    def update_version(self, version):
        self.version = version

    def __str__(self):
        return (
            f"{self.name} | "
            f"Model: {self.model} | "
            f"Version: {self.version}"
        )

agent = AIAgent("ResearchBot","gpt-5.5",1.0)
coding_agent = AIAgent("CodeBot", "gpt-5.5", 1.0)
tutor_agent = AIAgent("TutorBot", "gpt-5.5", 1.0)
agent.introduce()
agent.show_details()
coding_agent.introduce()
coding_agent.show_details()
tutor_agent.introduce()
tutor_agent.show_details()
agent.update_model("gpt-6.0")
agent.update_version(2.0)
print(agent)
