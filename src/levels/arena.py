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

class Arena(Scene):
    def __init__(self, modules: dict):
        super().__init__ # Initializes the scene

        self.modules = modules
        self.state_manager = modules["state"]
        self.input = modules["input"]
        self.ui = modules["ui"]
        self.sound = modules["sound"]
    def start(self):
        super().start()
        asset.get_image("arena.png")
        self.sound.play_sound("combat.mp3", 2500, True)
    def run(self):
        super().run
