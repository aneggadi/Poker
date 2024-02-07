import poker2
import random
import time
import tkinter as tk
import bot

# Create the main window
root = tk.Tk()
root.title("Poker Game")

# Initialize variables
baraja = [
    '2 ' + chr(3), '3 ' + chr(3), '4 ' + chr(3) , '5 ' + chr(3), '6 ' + chr(3), '7 ' + chr(3), '8 ' + chr(3),
    '9 ' + chr(3), '10 ' + chr(3), 'J ' + chr(3), 'Q ' + chr(3), 'K ' + chr(3), 'A ' + chr(3),
    '2 ' + chr(4), '3 ' + chr(4), '4 ' + chr(4), '5 ' + chr(4), '6 ' + chr(4), '7 ' + chr(4), '8 ' + chr(4),
    '9 ' + chr(4), '10 ' + chr(4), 'J ' + chr(4), 'Q ' + chr(4), 'K ' + chr(4), 'A ' + chr(4),
    '2 ' + chr(6), '3 ' + chr(6), '4 ' + chr(6), '5 ' + chr(6), '6 ' + chr(6), '7 ' + chr(6), '8 ' + chr(6),
    '9 ' + chr(6), '10 ' + chr(6), 'J ' + chr(6), 'Q ' + chr(6), 'K ' + chr(6), 'A ' + chr(6),
    '2 ' + chr(5), '3 ' + chr(5), '4 ' + chr(5), '5 ' + chr(5), '6 ' + chr(5), '7 ' + chr(5), '8 ' + chr(5),
    '9 ' + chr(5), '10 ' + chr(5), 'J ' + chr(5), 'Q ' + chr(5), 'K ' + chr(5), 'A ' + chr(5)
]
baraja1 = baraja
bote = 0
max_credito = 0

# Create label and entry for initial credit
credit_label = tk.Label(root, text="Credito inical:")
credit_label.grid(row=0, column=0)
credit_entry = tk.Entry(root, width=100)
credit_entry.grid(row=0, column=1)

def start_game():
    global max_credito
    max_credito = int(credit_entry.get())

    # Rest of the code
def button_pressed(event):
    print("Button pressed!")

root = tk.Tk()
button = tk.Button(root, text="Press me!")
button.pack()
button.bind("<Button-1>", button_pressed)

root.mainloop()
# Create button to start the game
start_button = tk.Button(root, text="Start game", command=start_game)

start_button.grid(row=1, column=0, columnspan=2)

# Rest of the code

root.mainloop()