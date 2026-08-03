class AIAgent:

    def __init__(self, name, model, version):
        self.name = name
        self.model = model
        self.version = version

    def introduce(self):
        print(f"Hello! I am {self.name}, running on {self.model} (Version {self.version}).")

    def update_model(self, new_model):
        self.model = new_model

    def update_version(self, version):
        self.version = version

class ResearchAgent(AIAgent):
        def __init__(self, name, model, version, specialty):
            super().__init__(name, model, version)
            self.specialty = specialty
    def introduce(self):
        print(self)
    def __str__(self):
        return (
            f"Hello! I am {self.name}.\n"
            f"Specialty: {self.specialty}\n"
            f"Running on {self.model}"
        )

agent = AIAgent("ResearchBot","gpt-5.5",1.0)
agent.update_model("gpt-6.0")
agent.update_version(2.0)
agent.introduce()
researchagent=ResearchAgent(
    "ResearchBot",
    "gpt-6",
    1.0,
    "Scientific Research"
    )
researchagent.introduce()
