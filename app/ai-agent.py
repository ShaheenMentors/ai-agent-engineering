class AIAgent:

    def __init__(self, name, model, version, status):
        self.name = name
        self.model = model
        self.version = version
        self.status = status

    def introduce(self):
        print(f"Hello! I am {self.name}, running on {self.model} (Version {self.version}).")

    def show_details(self):
        print("=" * 30)
        print(self)

    def update_model(self, new_model):
        self.model = new_model

    def update_version(self, version):
        self.version = version

    def __str__(self):
        return (
            f"{self.name} | "
            f"Model: {self.model} | "
            f"Version: {self.version} |"
            f"Status: {self.status}"
        )
    def activate(self):
        if self.status == "Inactive":
            self.status = "Active"
        print(self)
    
    def deactivate(self):
        if self.status == "Active":
            self.status = "Inactive"
        print(self)

agent = AIAgent("ResearchBot","gpt-5.5",1.0, "Active")
agent.update_model("gpt-6.0")
agent.update_version(2.0)
agent.deactivate()
agent.activate()
