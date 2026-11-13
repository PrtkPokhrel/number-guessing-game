
import tkinter as tk

from config.settings import *
from screens.home_screen import HomeScreen
from screens.game_screen import GameScreen


class NumberGuessingGame:

    def __init__(self, root):

        self.root = root

        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

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

        # Start at home screen
        self.show_home()

        # Enter key support
        self.root.bind(
            "<Return>",
            self.handle_enter
        )

    def show_home(self):

        self.game_screen.hide()
        self.home_screen.show()

    def show_game(self):

        self.home_screen.hide()
        self.game_screen.restart_game()
        self.game_screen.show()

    def handle_enter(self, event):

        if self.game_screen.frame.winfo_ismapped():
            self.game_screen.check_user_guess()

    def quit_game(self):

        self.root.destroy()


# Start application
if __name__ == "__main__":

    root = tk.Tk()

    app = NumberGuessingGame(root)

    root.mainloop()








"""

import random

# Generate a random number
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret_number:
        print("Too high! Try again.")

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Congratulations! You guessed the correct number!")
        break

print("Game over!")
"""



"""


import tkinter as tk
import random

# Game variables
secret_number = random.randint(1, 10)
attempts = 0

# Functions
def check_guess():
    global attempts

    user_input = guess_entry.get()

    if not user_input.isdigit():
        result_label.config(text="Please enter a valid number!", fg="#ff6b6b")
        return

    guess = int(user_input)

    if guess < 1 or guess > 100:
        result_label.config(text="Enter a number between 1 and 10!", fg="#ff6b6b")
        return

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    if guess < secret_number:
        result_label.config(text="Too low! Try a higher number.", fg="#fbbf24")

    elif guess > secret_number:
        result_label.config(text="Too high! Try a lower number.", fg="#fbbf24")

    else:
        result_label.config(
            text=f"🎉 Correct! You won in {attempts} attempts!",
            fg="#4ade80"
        )
        guess_button.config(state="disabled")

    guess_entry.delete(0, tk.END)


def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    attempts_label.config(text="Attempts: 0")
    result_label.config(text="Make your first guess!", fg="#ffffff")
    guess_button.config(state="normal")
    guess_entry.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#171923")

# Main title
title_label = tk.Label(
    root,
    text="NUMBER GUESSING GAME",
    font=("Arial", 20, "bold"),
    bg="#171923",
    fg="#a78bfa"
)
title_label.pack(pady=(35, 10))

# Instructions
instruction_label = tk.Label(
    root,
    text="I'm thinking of a number between 1 and 100.",
    font=("Arial", 11),
    bg="#171923",
    fg="#cbd5e1"
)
instruction_label.pack(pady=10)

# Input label
input_label = tk.Label(
    root,
    text="Enter your guess",
    font=("Arial", 12),
    bg="#171923",
    fg="white"
)
input_label.pack(pady=(25, 8))

# Input box
guess_entry = tk.Entry(
    root,
    font=("Arial", 20),
    justify="center",
    width=12,
    bg="#2d3748",
    fg="white",
    insertbackground="white",
    relief="flat"
)
guess_entry.pack(ipady=10)
guess_entry.focus()

# Guess button
guess_button = tk.Button(
    root,
    text="GUESS",
    font=("Arial", 12, "bold"),
    bg="#8b5cf6",
    fg="white",
    activebackground="#7c3aed",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=check_guess
)
guess_button.pack(pady=20, ipadx=45, ipady=8)

# Result message
result_label = tk.Label(
    root,
    text="Make your first guess!",
    font=("Arial", 12, "bold"),
    bg="#171923",
    fg="white"
)
result_label.pack(pady=10)

# Attempts counter
attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 12),
    bg="#171923",
    fg="#a78bfa"
)
attempts_label.pack(pady=10)

# Restart button
restart_button = tk.Button(
    root,
    text="RESTART GAME",
    font=("Arial", 10, "bold"),
    bg="#374151",
    fg="white",
    activebackground="#4b5563",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=restart_game
)
restart_button.pack(pady=20, ipadx=25, ipady=7)

# Press Enter to guess
root.bind("<Return>", lambda event: check_guess())

# Run the application
root.mainloop()


"""


"""
 

import tkinter as tk
import random

# Game variables
secret_number = 0
attempts = 0


# -----------------------------
# SCREEN MANAGEMENT
# -----------------------------

def show_home_screen():
    game_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)


def show_game_screen():
    home_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    restart_game()


def quit_game():
    root.destroy()


# -----------------------------
# GAME FUNCTIONS
# -----------------------------

def check_guess():
    global attempts

    user_input = guess_entry.get()

    if not user_input.isdigit():
        result_label.config(
            text="Please enter a valid number!",
            fg="#ff6b6b"
        )
        return

    guess = int(user_input)

    if guess < 1 or guess > 100:
        result_label.config(
            text="Enter a number between 1 and 100!",
            fg="#ff6b6b"
        )
        return

    attempts += 1
    attempts_label.config(text=f"Attempts: {attempts}")

    if guess < secret_number:
        result_label.config(
            text="Too low! Try a higher number.",
            fg="#fbbf24"
        )

    elif guess > secret_number:
        result_label.config(
            text="Too high! Try a lower number.",
            fg="#fbbf24"
        )

    else:
        result_label.config(
            text=f"Correct! You won in {attempts} attempts!",
            fg="#4ade80"
        )
        guess_button.config(state="disabled")

    guess_entry.delete(0, tk.END)


def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    attempts_label.config(text="Attempts: 0")
    result_label.config(
        text="Make your first guess!",
        fg="white"
    )

    guess_button.config(state="normal")
    guess_entry.delete(0, tk.END)
    guess_entry.focus()


# -----------------------------
# MAIN WINDOW
# -----------------------------

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x500")
root.resizable(False, False)
root.configure(bg="#171923")


# -----------------------------
# HOME SCREEN
# -----------------------------

home_frame = tk.Frame(root, bg="#171923")

title_label = tk.Label(
    home_frame,
    text="NUMBER\nGUESSING GAME",
    font=("Arial", 25, "bold"),
    bg="#171923",
    fg="#a78bfa",
    justify="center"
)
title_label.pack(pady=(100, 30))

subtitle_label = tk.Label(
    home_frame,
    text="Test your luck and guessing skills!",
    font=("Arial", 11),
    bg="#171923",
    fg="#cbd5e1"
)
subtitle_label.pack(pady=10)

play_button = tk.Button(
    home_frame,
    text="PLAY GAME",
    font=("Arial", 13, "bold"),
    bg="#8b5cf6",
    fg="white",
    activebackground="#7c3aed",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=show_game_screen
)
play_button.pack(pady=(35, 15), ipadx=45, ipady=10)

quit_button = tk.Button(
    home_frame,
    text="QUIT GAME",
    font=("Arial", 11, "bold"),
    bg="#374151",
    fg="white",
    activebackground="#4b5563",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=quit_game
)
quit_button.pack(pady=10, ipadx=40, ipady=8)


# -----------------------------
# GAME SCREEN
# -----------------------------

game_frame = tk.Frame(root, bg="#171923")

game_title = tk.Label(
    game_frame,
    text="NUMBER GUESSING GAME",
    font=("Arial", 20, "bold"),
    bg="#171923",
    fg="#a78bfa"
)
game_title.pack(pady=(35, 10))

instruction_label = tk.Label(
    game_frame,
    text="I'm thinking of a number between 1 and 100.",
    font=("Arial", 11),
    bg="#171923",
    fg="#cbd5e1"
)
instruction_label.pack(pady=10)

input_label = tk.Label(
    game_frame,
    text="Enter your guess",
    font=("Arial", 12),
    bg="#171923",
    fg="white"
)
input_label.pack(pady=(25, 8))

guess_entry = tk.Entry(
    game_frame,
    font=("Arial", 20),
    justify="center",
    width=12,
    bg="#2d3748",
    fg="white",
    insertbackground="white",
    relief="flat"
)
guess_entry.pack(ipady=10)

guess_button = tk.Button(
    game_frame,
    text="GUESS",
    font=("Arial", 12, "bold"),
    bg="#8b5cf6",
    fg="white",
    activebackground="#7c3aed",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=check_guess
)
guess_button.pack(pady=20, ipadx=45, ipady=8)

result_label = tk.Label(
    game_frame,
    text="Make your first guess!",
    font=("Arial", 12, "bold"),
    bg="#171923",
    fg="white"
)
result_label.pack(pady=10)

attempts_label = tk.Label(
    game_frame,
    text="Attempts: 0",
    font=("Arial", 12),
    bg="#171923",
    fg="#a78bfa"
)
attempts_label.pack(pady=10)

restart_button = tk.Button(
    game_frame,
    text="RESTART GAME",
    font=("Arial", 10, "bold"),
    bg="#374151",
    fg="white",
    activebackground="#4b5563",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=restart_game
)
restart_button.pack(pady=10, ipadx=25, ipady=7)

home_button = tk.Button(
    game_frame,
    text="BACK TO HOME",
    font=("Arial", 10, "bold"),
    bg="#374151",
    fg="white",
    activebackground="#4b5563",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=show_home_screen
)
home_button.pack(pady=5, ipadx=25, ipady=7)


# Keyboard support
root.bind("<Return>", lambda event: check_guess())

# Start at home screen
show_home_screen()

# Run application
root.mainloop()


"""