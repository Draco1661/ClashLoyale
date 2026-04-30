import pygame
def auto_scaling():
    """
    called at startup
    display fullscreen game and use this fullscreen to get the size of the screen
    if the screen is too small return True, if not return False
    """
    pygame.display.toggle_fullscreen() # fullscreen
    w, h = pygame.display.get_surface().get_size() # utilise le fait que c'est en fullscreen pour récuperer la taille de l'écran
    if w < 1000 or h < 1000:
        w2 = int(1000/100 * w)
        h2 = int(1000/100 * h)
        return w2, h2
    else:
        return False