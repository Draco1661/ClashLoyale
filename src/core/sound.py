import logging
from pathlib import Path

import pygame
from pygame.event import Event
from pygame.mixer import Channel

import constant
from core import asset
from utils import log


class Sound:
    def __init__(self, channel_count: int) -> None:
        """
        Sound module.
        
        :param channel_count: Number of sound channels to be available. 
        :rtype: None
        """
        
        self.channel_count = channel_count
        self.channels: list[Channel] = []

        try:
            pygame.mixer.init()
            pygame.mixer.set_num_channels(self.channel_count)

            self.channels = [pygame.mixer.Channel(channel_index) for channel_index in range(channel_count)]

            self.initialized = True
            log.logger.send(f"Initialized sound system with {channel_count} channels.")
        except pygame.error as e:
            if "WASAPI" in str(e):
                self.initialized = False
                log.logger.send("Failed to initialize sound system.", logging.WARNING)

    def get_channel(self) -> pygame.mixer.Channel | None:
        """
        Gets an available, non-busy channel.
        
        :return: An available channel. None if there's no available channel.
        :rtype: pygame.mixer.Channel | None
        """

        for channel in self.channels:
            if not channel.get_busy():
                return channel
        return None

    def play_sound(self, path: Path, fade_in: int, looped: bool = False) -> int:
        """
        Plays a given sound.
        
        :param path: Path where the sound is stored.
        :param fade_in: Fade in time in milliseconds of the sound.
        :param looped: Whether the sound should be looped or not.
        :return: Result state, -1 if failed, 0 otherwise.
        :rtype: int
        """

        if not self.initialized:
            log.logger.send("Sound is not initialized.", logging.WARNING)
            return 0

        path = constant.MUSIC_THEMES_PATH / path
        channel = self.get_channel()
        sound = asset.get_sound(path)
        loops = -1 if looped else 0
        
        if channel is None:
            log.logger.send(f"Could not play sound from {path}, there is no channel available.", logging.ERROR)
            return -1
        
        channel.play(sound, loops, 0, fade_in)
        log.logger.send(f"Playing {path}.", logging.DEBUG)

        return 0

    def stop_sound(self, channel) -> None:
        """
        Stop channel's playback.
        
        :rtype: None
        :param channel: The channel to stop playing.
        """
        if type(channel) is list(Channel):
            for c in channel:
                if channel.get_busy():
                    c.stop()
        elif type(channel) is Channel:
            if channel.get_busy():
                channel.stop()
        
        if channel.get_busy():
            pygame.mixer.music.stop()
            log.logger.send("Stopped current music.", logging.DEBUG)
        else:
            log.logger.send("No music is playing, cannot stop.", logging.WARNING)

    def rewind_sound(self, channel: Channel) -> None:
        """
        Rewind channel's playback.
        
        :param channel: The channel to rewind playing.
        :rtype: None
        """

        if not channel.get_busy():
            log.logger.send("No music is playing, cannot rewind.", logging.WARNING)
        else:
            pygame.mixer.music.rewind()
            log.logger.send("Rewind current music.", logging.DEBUG)

    def tick(self, events: list[Event]):
        pass

    def on_state_change(self):
        self.stop_sound()
