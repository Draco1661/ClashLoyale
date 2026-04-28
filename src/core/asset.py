import logging
from pathlib import Path

import pygame

from utils import log

__images: dict[Path, pygame.Surface] = {}
__fonts: dict[str, pygame.font.Font] = {}
__sounds: dict[Path, pygame.mixer.Sound] = {}


# Image
def get_image(path: Path) -> pygame.Surface:
    """
    Stores the image to memory the first time for re-use.

    Args:
        path (pathlib.Path): The path where the image is stored.

    Returns:
        pygame.Surface: An instance of the image's surface.
    """

    if path not in __images.keys():
        try:
            image = pygame.image.load(path)
        except pygame.error:
            log.logger.send(f"Could not load image {path} as it was not found.", logging.ERROR)

        log.logger.send(f"Loaded image {path}", logging.DEBUG)
        __images[path] = image
        return image
    else:
        log.logger.send(f"Retrieved image {path}", logging.DEBUG)
        return __images[path]


def clear_image(path: Path) -> bool:
    """
    Clears the image from memory if found. 
    Use this if you are sure you won't need it anymore to decrease memory usage.

    Args:
        path (pathlib.Path): The path where the image is stored.

    Returns:
        bool: Whether it was found and deleted or not.
    """

    try:
        del __images[path]
        return True
    except KeyError:
        return False


# Font
def get_font(path: Path, size: int) -> pygame.font.Font:
    """
    Stores the font to memory the first time for re-use.

    Args:
        path (pathlib.Path): The path where the font is stored.
        size (int): The size the font will have.

    Returns:
        pygame.font.Font: An instance of the font.
    """

    index = f"{path}{size}"
    if path not in __fonts.keys():
        try:
            font = pygame.font.Font(path, size)
        except pygame.error:
            log.logger.send(f"Could not load font {path} as it was not found.", logging.ERROR)

        log.logger.send(f"Loaded font {path} of size {size}", logging.DEBUG)
        __fonts[index] = font
        return font
    else:
        log.logger.send(f"Retrieved font {path}", logging.DEBUG)
        return __fonts[index]


def clear_font(path: Path) -> bool:
    """
    Clears the font from memory if found.
    Use this if you are sure you won't need it anymore to decrease memory usage.
    
    Args:
        path (pathlib.Path): The path where the font is stored.

    Returns:
        bool: Whether the font was found and deleted or not.
    """

    try:
        del __fonts[str(path)]
        return True
    except KeyError:
        return False


# Sound
def get_sound(path: Path) -> pygame.mixer.Sound:
    """
    Stores the sound to memory the first time for re-use.

    Args:
        path (pathlib.Path): The path where the sound is stored.

    Returns:
        pygame.mixer.Sound: An instance of the sound.
    """

    if path not in __sounds.keys():
        try:
            sound = pygame.mixer.Sound(path)
        except pygame.error:
            log.logger.send(f"Could not load sound {path} as it was not found.", logging.ERROR)

        log.logger.send(f"Loaded sound {path}", logging.DEBUG)
        __sounds[path] = sound
        return sound
    else:
        log.logger.send(f"Retrieved sound {path}", logging.DEBUG)
        return __sounds[path]


def clear_sound(path: Path) -> bool:
    """
    Clears the sound from memory if found.
    Use this if you are sure you won't need it anymore to decrease memory usage.

    Args:
        path (pathlib.Path): The path where the sound is stored.

    Returns:
        bool: Whether the sound was found and deleted or not.
    """

    try:
        del __sounds[path]
        return True
    except KeyError:
        return False

# reference: https://www.pygame.org/pcr/caching_resource/index.php
