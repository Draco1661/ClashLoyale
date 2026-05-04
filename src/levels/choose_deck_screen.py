import constant
import pygame
import os
import logging

from core import asset
from utils import log
from levels.widgets.button_widget import ButtonWidget
deck_blue_selection=[]


class ChooseDeckScreen:
    def __init__(self, modules):
        self.ui = modules["ui"]
        self.screen = self.ui.screen
        self.chosen = 0
        self.cartes=[]

        self.ready_image = asset.get_image(constant.GUI_PATH / "ready.png").convert_alpha()
        self.ready_image = pygame.transform.scale(self.ready_image, (self.screen.get_width() / 5.7, self.screen.get_height() / 13))

        for file in os.listdir(constant.CARDS_PATH):
            if file.endswith(".png"):
                image = asset.get_image(constant.CARDS_PATH / file).convert_alpha()
                image = pygame.transform.scale(image, (self.screen.get_width() / 10.5, self.screen.get_height() / 9))
                self.cartes.append(image)

        self.screen.fill(constant.BACKGROUND_COLOR)

        x=80
        y=200
        for carte in self.cartes:
            if x > self.screen.get_width() - 150:
                x=80
                y+=130
            
            component = ButtonWidget(
                modules,
                (x,y),
                carte,
                lambda: self.ajout_carte()
            )
            
            self.ui.add_component(component)

            x+=120

    def run(self):
        self.screen.blit(self.ready_image, (self.screen.get_width() / 1.5, self.screen.get_width() / 1.2))
        pass # TODO: PUT HERE AFTER


    def ajout_carte(self):
        if self.chosen==0:
            self.chosen = 1
            print("carte add")
            deck_blue_selection.append("carte")
        else :
            self.chosen = 0
            print("carte pop")
            del deck_blue_selection[0]
        print(deck_blue_selection)