Python
class AutomationScript:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def __str__(self):
        return f"Automation Script: {self.name}\nDescription: {self.description}\nSteps: {', '.join(str(step) for step in self.steps)}"


class Step:
    def __init__(self, action, target, value):
        self.action = action
        self.target = target
        self.value = value

    def __str__(self):
        return f"{self.action} {self.target} with {self.value}"


class Parser:
    def __init__(self):
        self.scripts = {}

    def parse_script(self, script_text):
        lines = script_text.splitlines()
        script_name = lines[0].strip()
        script_description = lines[1].strip()
        script = AutomationScript(script_name, script_description)

        for line in lines[2:]:
            parts = line.strip().split(',')
            action = parts[0].strip()
            target = parts[1].strip()
            value = parts[2].strip()
            script.add_step(Step(action, target, value))

        self.scripts[script_name] = script

    def get_script(self, script_name):
        return self.scripts.get(script_name)


# Example usage
parser = Parser()
script_text = """My Script
This is a sample script
click, button, submit
type, input, username
wait, 5, seconds
"""
parser.parse_script(script_text)
print(parser.get_script("My Script"))