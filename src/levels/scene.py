import constant
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
        self.ui.screen.fill(constant.BACKGROUND_COLOR)
    
    @abstractmethod
    def run(self) -> None:
        """
        Runs every frame upon scene activation
        """

