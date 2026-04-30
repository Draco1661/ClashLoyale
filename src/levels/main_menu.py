import pygame

from constant import WIDGETS_PATH
from core import asset
from core.state import GameState
from levels.widgets.ButtonWithTipWidget import ButtonWithTipWidget
from levels.widgets.centered_text_widget import CenteredTextWidget
from levels.scene import Scene


def blank(widget):
    pass

def test_id(widget):
    print(f"Got ID {widget.id}")

class MainMenu(Scene):
    def __init__(self, modules: dict):
        super().__init__ # Initializes the scene

        self.modules = modules
        self.state_manager = modules["state"]
        self.input = modules["input"]
        self.ui = modules["ui"]
        self.sound = modules["sound"]

            
    def start(self):
        super().start()

        play_sprite = asset.get_image(WIDGETS_PATH / 'play_icon.png').convert_alpha()
        play_sprite = pygame.transform.scale(play_sprite, (96, 96))

        components = [
            ButtonWithTipWidget(
                self.modules,
                "Play",
                self.ui.font_medium,
                (25, self.ui.screen_height - 100),
                play_sprite,
                lambda: self.state_manager.set_state(GameState.DECK_SELECTION)
            ),

            CenteredTextWidget(
                self.modules,
                "Clash Loyale",
                self.ui.font_large,
                (self.ui.screen_width / 2, 30),
            )
        ]

        for component in components:
            self.ui.add_component(component)

        self.sound.play_sound("deck.mp3", 2500, True)

    def run(self):
        super().run
