
import pygame
from pathlib import Path

from config.settings import MUSIC_VOLUME

# Locate the music folder
MUSIC_FOLDER = Path(__file__).parent / "music"


def init_audio():
    """Initialize the audio system."""
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
    except pygame.error as error:
        print(f"Audio initialization failed: {error}")


def play_music(filename):
    """Play a music file continuously."""
    try:
        init_audio()

        music_path = MUSIC_FOLDER / filename

        pygame.mixer.music.stop()
        pygame.mixer.music.load(str(music_path))
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

    except (pygame.error, OSError) as error:
        print(f"Could not play music: {error}")


def stop_music():
    """Stop the currently playing music."""
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
