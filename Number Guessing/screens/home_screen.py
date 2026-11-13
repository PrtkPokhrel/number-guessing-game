
import tkinter as tk

from config.settings import *


class HomeScreen:

    def __init__(self, parent, on_play, on_quit):

        self.frame = tk.Frame(parent, bg=BACKGROUND)

        title_label = tk.Label(
            self.frame,
            text="NUMBER\nGUESSING GAME",
            font=("Arial", 25, "bold"),
            bg=BACKGROUND,
            fg=PRIMARY,
            justify="center"
        )
        title_label.pack(pady=(100, 30))

        subtitle_label = tk.Label(
            self.frame,
            text="Test your luck and guessing skills!",
            font=NORMAL_FONT,
            bg=BACKGROUND,
            fg=SECONDARY_TEXT
        )
        subtitle_label.pack(pady=10)

        play_button = tk.Button(
            self.frame,
            text="PLAY GAME",
            font=BUTTON_FONT,
            bg=PRIMARY,
            fg=TEXT_COLOR,
            activebackground=PRIMARY_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=on_play
        )
        play_button.pack(pady=(35, 15), ipadx=45, ipady=10)

        quit_button = tk.Button(
            self.frame,
            text="QUIT GAME",
            font=("Arial", 11, "bold"),
            bg=BUTTON_BACKGROUND,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=on_quit
        )
        quit_button.pack(pady=10, ipadx=40, ipady=8)

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def hide(self):
        self.frame.pack_forget()
