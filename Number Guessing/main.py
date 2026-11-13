
import tkinter as tk

from config.settings import *
from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen

from audio.music_manager import (
    init_audio,
    play_music,
    stop_music
)


class NumberGuessingGame:

    def __init__(self, root):

        self.root = root

        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

        # Initialize audio
        init_audio()

        # Create screens
        self.home_screen = HomeScreen(
            self.root,
            on_play=self.show_game,
            on_quit=self.quit_game
        )

        self.game_screen = GameScreen(
            self.root,
            on_home=self.show_home
        )

        # Start at home
        self.show_home()

        # Enter key support
        self.root.bind(
            "<Return>",
            self.handle_enter
        )

        # Handle window close button
        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.quit_game
        )

    def show_home(self):

        self.game_screen.hide()
        self.home_screen.show()

        # Play home screen music
        play_music("home.mp3")

    def show_game(self):

        self.home_screen.hide()

        self.game_screen.restart_game()
        self.game_screen.show()

        # Play gameplay music
        play_music("gameplay.mp3")

    def handle_enter(self, event):

        if self.game_screen.frame.winfo_ismapped():
            self.game_screen.check_user_guess()

    def quit_game(self):

        stop_music()
        self.root.destroy()


if __name__ == "__main__":

    root = tk.Tk()

    app = NumberGuessingGame(root)

    root.mainloop()
