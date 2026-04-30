import pygame
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
    if largeur < 1000 or hauteur < 1000:
        w2 = int(1000/100 * largeur)
        h2 = int(1000/100 * hauteur)
        return w2, h2
    else:
        return False