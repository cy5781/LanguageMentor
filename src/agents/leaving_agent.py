from .base_scenario_agent import ScenarioAgent

class LeavingAgent(ScenarioAgent):
    def __init__(self):
        super().__init__()
        self.name = "Leaving Agent"

    def respond(self, user_input):
        # 调用与请假相关的逻辑
        return f"Leaving Agent Response: {user_input}"
