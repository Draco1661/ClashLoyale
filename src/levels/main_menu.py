import pygame
import constant

from core import asset
from core.state import GameState
from levels.widgets.button_widget import ButtonWidget
from levels.scene import Scene
from levels.widgets.button_with_tip_widget import ButtonWithTipWidget
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

        play_sprite = asset.get_image(constant.WIDGETS_PATH / 'play_icon.png').convert_alpha()
        play_sprite = pygame.transform.scale(play_sprite, (96, 96))

        components = [
            ButtonWidget(
                self.modules,
                (35, constant.SCREEN_HEIGHT - 120),
                play_sprite,
                lambda _: self.state_manager.set_state(GameState.DECK_SELECTION)
            )
        ]

        self.background_image = asset.get_image(constant.GUI_PATH / "loading_cl.png").convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
        self.ui.screen.blit(self.background_image,(0,0))

        for component in components:
            self.ui.add_component(component)

        self.sound.play_sound("deck.mp3", 2500, True)

    def run(self):
        super().run
