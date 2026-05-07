import pygame
import constant
from core import asset
from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, modules: dict):
        self.modules = modules
        self.ui = self.modules["ui"]


    @abstractmethod
    def start(self) -> None:
        """
        Runs once upon scene activation.
        """
        self.ui.clear_components()
        self.background_image = asset.get_image(constant.GUI_PATH / "fond.png").convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
        self.ui.screen.blit(self.background_image,(0,0))

    @abstractmethod
    def run(self) -> None:
        """
        Runs every frame upon scene activation
        """

