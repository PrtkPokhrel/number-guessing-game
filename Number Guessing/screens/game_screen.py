
import tkinter as tk
from tkinter import messagebox, simpledialog

from config.settings import *
from game.logic import (
    generate_number,
    check_guess,
    generate_math_question,
    generate_hint
)


class GameScreen:

    def __init__(self, parent, on_home):

        self.frame = tk.Frame(parent, bg=BACKGROUND)

        self.on_home = on_home

        self.secret_number = 0
        self.attempts = 0
        self.hint_used = False

        # Title
        title_label = tk.Label(
            self.frame,
            text="NUMBER GUESSING GAME",
            font=TITLE_FONT,
            bg=BACKGROUND,
            fg=PRIMARY
        )
        title_label.pack(pady=(35, 10))

        # Instructions
        instruction_label = tk.Label(
            self.frame,
            text=f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.",
            font=NORMAL_FONT,
            bg=BACKGROUND,
            fg=SECONDARY_TEXT
        )
        instruction_label.pack(pady=10)

        # Input label
        input_label = tk.Label(
            self.frame,
            text="Enter your guess",
            font=("Arial", 12),
            bg=BACKGROUND,
            fg=TEXT_COLOR
        )
        input_label.pack(pady=(25, 8))

        # Input field
        self.guess_entry = tk.Entry(
            self.frame,
            font=("Arial", 20),
            justify="center",
            width=12,
            bg=INPUT_BACKGROUND,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat"
        )
        self.guess_entry.pack(ipady=10)

        # Guess button
        self.guess_button = tk.Button(
            self.frame,
            text="GUESS",
            font=BUTTON_FONT,
            bg=PRIMARY,
            fg=TEXT_COLOR,
            activebackground=PRIMARY_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=self.check_user_guess
        )
        self.guess_button.pack(pady=20, ipadx=45, ipady=8)

        # Hint button
        self.hint_button = tk.Button(
            self.frame,
            text="GET HINT",
            font=("Arial", 10, "bold"),
            bg=BUTTON_BACKGROUND,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=self.request_hint
        )
        self.hint_button.pack(pady=5, ipadx=25, ipady=7)

        # Result message
        self.result_label = tk.Label(
            self.frame,
            text="Make your first guess!",
            font=("Arial", 12, "bold"),
            bg=BACKGROUND,
            fg=TEXT_COLOR
        )
        self.result_label.pack(pady=10)

        # Attempts counter
        self.attempts_label = tk.Label(
            self.frame,
            text="Attempts: 0",
            font=("Arial", 12),
            bg=BACKGROUND,
            fg=PRIMARY
        )
        self.attempts_label.pack(pady=10)

        # Restart button
        restart_button = tk.Button(
            self.frame,
            text="RESTART GAME",
            font=("Arial", 10, "bold"),
            bg=BUTTON_BACKGROUND,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=self.restart_game
        )
        restart_button.pack(pady=10, ipadx=25, ipady=7)

        # Home button
        home_button = tk.Button(
            self.frame,
            text="BACK TO HOME",
            font=("Arial", 10, "bold"),
            bg=BUTTON_BACKGROUND,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            cursor="hand2",
            command=self.on_home
        )
        home_button.pack(pady=5, ipadx=25, ipady=7)

        # Start a new game
        self.restart_game()

    def request_hint(self):

        # Check whether the hint was already used
        if self.hint_used:
            messagebox.showinfo(
                "Hint",
                "You have already used your hint!"
            )
            return

        # Generate a maths question
        question, correct_answer = generate_math_question()

        # Ask the player to solve it
        user_answer = simpledialog.askinteger(
            "Math Challenge",
            f"Solve this question to unlock your hint:\n\n{question}",
            parent=self.frame
        )

        # Player cancelled
        if user_answer is None:
            return

        # Check the answer
        if user_answer == correct_answer:

            hint = generate_hint(self.secret_number)

            messagebox.showinfo(
                "Hint Unlocked!",
                f"Congratulations! Here's your hint:\n\n{hint}"
            )

            self.hint_used = True
            self.hint_button.config(state="disabled")

        else:
            messagebox.showerror(
                "Incorrect Answer",
                "Oops! That's incorrect.\nYou didn't unlock the hint."
            )

    def check_user_guess(self):

        user_input = self.guess_entry.get()

        if not user_input.isdigit():
            self.result_label.config(
                text="Please enter a valid number!",
                fg=ERROR_COLOR
            )
            return

        guess = int(user_input)

        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            self.result_label.config(
                text=f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}!",
                fg=ERROR_COLOR
            )
            return

        self.attempts += 1

        self.attempts_label.config(
            text=f"Attempts: {self.attempts}"
        )

        result = check_guess(guess, self.secret_number)

        if result == "low":
            self.result_label.config(
                text="Too low! Try a higher number.",
                fg=WARNING_COLOR
            )

        elif result == "high":
            self.result_label.config(
                text="Too high! Try a lower number.",
                fg=WARNING_COLOR
            )

        else:
            self.result_label.config(
                text=f"Correct! You won in {self.attempts} attempts!",
                fg=SUCCESS_COLOR
            )

            self.guess_button.config(state="disabled")
            self.hint_button.config(state="disabled")

        self.guess_entry.delete(0, tk.END)

    def restart_game(self):

        self.secret_number = generate_number()
        self.attempts = 0
        self.hint_used = False

        self.attempts_label.config(text="Attempts: 0")

        self.result_label.config(
            text="Make your first guess!",
            fg=TEXT_COLOR
        )

        self.guess_button.config(state="normal")
        self.hint_button.config(state="normal")

        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def show(self):
        self.frame.pack(fill="both", expand=True)
        self.guess_entry.focus()

    def hide(self):
        self.frame.pack_forget()
