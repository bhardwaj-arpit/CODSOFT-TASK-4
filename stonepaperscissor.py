import tkinter as tk
from tkinter import messagebox
import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"


def on_play():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    result_text = f"User chose: {user_choice}\nComputer chose: {computer_choice}\n"
    if winner == "tie":
        result_text += "It's a tie!"
    elif winner == "user":
        result_text += "You win!"
    else:
        result_text += "Computer wins!"

    messagebox.showinfo("Result", result_text)


def create_gui():
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    # User choice input
    tk.Label(root, text="Choose Rock, Paper, or Scissors:").pack(pady=5)
    global user_choice_var
    user_choice_var = tk.StringVar(value="rock")
    choices = ["rock", "paper", "scissors"]
    for choice in choices:
        tk.Radiobutton(root, text=choice.capitalize(), variable=user_choice_var, value=choice).pack(anchor=tk.W)

    # Play button
    tk.Button(root, text="Play", command=on_play).pack(pady=10)

    # Exit button
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
