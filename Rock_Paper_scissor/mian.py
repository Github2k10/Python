import random
import tkinter as tk
from tkinter import messagebox

choices = ['rock', 'paper', 'scissors', 'lizard', 'Spock']


def play_game(player_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    messagebox.showinfo("Game Result", f"You chose {player_choice}\nComputer chose {computer_choice}\n\n{result}")


def determine_winner(player_choice, computer_choice):
    if computer_choice == player_choice:
        return "Match Draw"
    elif (player_choice == "rock" and computer_choice == "scissor") or (
            player_choice == "scissor" and computer_choice == "paper") or (
            player_choice == "paper" and computer_choice == "rock") or (
            player_choice == "rock" and computer_choice == "lizard") or (
            player_choice == "lizard" and computer_choice == "spock") or (
            player_choice == "spock" and computer_choice == "scissor") or (
            player_choice == "scissor" and computer_choice == "lizard") or (
            player_choice == "lizard" and computer_choice == "paper") or (
            player_choice == "paper" and computer_choice == "spock") or (
            player_choice == "spock" and computer_choice == "rock"):
        return "You won"
    else:
        return "You lose"


window = tk.Tk()
window.title("Welcome to the game rock, paper, scissor, lizard, Spock...")

label = tk.Label(window, text="Select your choice:")
label.pack()

for choice in choices:
    button = tk.Button(window, text=choice, command=lambda player_choice=choice: play_game(player_choice))
    button.pack()

quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack()

window.mainloop()
