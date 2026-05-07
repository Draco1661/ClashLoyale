from core import asset
from constant import SPRITES_PATH
from levels.scene import Scene
from levels.widgets.button_with_tip_widget import ButtonWithTipWidget
from levels.widgets.image_widget import ImageWidget
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
            ), # TODO: Add other modules as test
            ImageWidget(
                self.modules,
                (100,100),
                asset.get_image(SPRITES_PATH / "arena.png"),
                id="ImageWidgetTest"
            )
        ]
        
        for component in components:
            self.ui.add_component(component)

    def run(self):
        super().run()
        
