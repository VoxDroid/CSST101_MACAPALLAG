scenario = "environment" #@param ["game", "environment"] {allow-input: true}

class SimpleAI:
    def __init__(self, scenario):
        """
        Initialize the AI agent with a scenario.
        
        :param scenario: str, defines the context of decision-making.
        """
        self.scenario = scenario

    def decide(self, conditions):
        """
        Decide an action based on the current conditions and scenario.
        
        :param conditions: dict, mapping conditions to their truth values.
        :return: str, the chosen action.
        """
        if self.scenario == "game":
            if conditions['has_enemy']:
                return "Attack"
            elif conditions['has_resources']:
                return "Gather Resources"
            else:
                return "Explore"
        elif self.scenario == "environment":
            if conditions['weather'] == "rainy":
                return "Stay Inside"
            elif conditions['weather'] == "sunny":
                return "Go Out"
            else:
                return "Check Weather"