import pygame
import constant
from utils import log
def auto_scaling():
    """
    called at startup
    display fullscreen game and use this fullscreen to get the size of the screen
    if the screen is too small return True, if not return False
    """
    size = pygame.display.get_desktop_sizes()
    largeur = size[0][0]
    hauteur = size[0][1]
    log.logger.send("size of the screen")
    log.logger.send(str(size))
    #pygame.display.toggle_fullscreen() # fullscreen
    #w, h = pygame.display.get_surface().get_size() # utilise le fait que c'est en fullscreen pour récuperer la taille de l'écran
    if largeur < constant.SCREEN_WIDTH or hauteur < constant.SCREEN_HEIGHT:
        w2 = int(SCREEN_WITDH / 2)
        h2 = int(SCREEN_HEIGHT / 2)
        return w2, h2
    else:
        return False
