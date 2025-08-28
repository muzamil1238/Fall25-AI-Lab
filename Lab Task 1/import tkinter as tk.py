import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
        [0, 4, 8, 12],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [0, 5, 10, 15],
        [3, 6, 9, 12]
    ]:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] == buttons[combo[3]]["text"] != ""):
            
            for index in combo:
                buttons[index].config(bg="green")
            messagebox.showinfo("tic-tac-toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                     command=lambda i=i: button_click(i)) for i in range(16)]

for i, button in enumerate(buttons):
    button.grid(row=i // 4, column=i % 4)

current_player = "X"
winner = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=4, column=0, columnspan=4)

root.mainloop()
