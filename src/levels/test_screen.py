from core.state import StateManager


class TestScreen:
    def __init__(self, modules: dict):
        # Module definitions
        self.ui = modules["ui"]

    def run(self):
        self.ui.screen.fill('red')
