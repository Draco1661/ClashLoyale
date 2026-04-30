from levels.scene import Scene
from levels.widgets.ButtonWithTipWidget import ButtonWithTipWidget
from levels.widgets.text_widget import TextWidget

class TestScreen(Scene):
    def __init__(self, modules: dict):
        super().__init__

        # Module definitions
        self.modules = modules
        self.ui = self.modules["ui"]

    def start(self):
        super().start()

        components = [
            TextWidget(
                self.modules,
                "TextWidget",
                self.ui.font_small,
                (50, 50)
            ) # TODO: Add other modules as test
        ]
        
        for component in components:
            self.ui.add_component(component)

    def run(self):
        super().run()
        
