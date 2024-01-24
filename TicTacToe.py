from tkinter import *
import random


def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = players[0]
            if check_winner() is False:
                player = players[1]
                theLabel.config(text= players[1] + " Turn")
            elif check_winner():
                theLabel.config(text= players[0] + " Win!")
            elif check_winner() == "Tie":
                theLabel.config(text="Tie!")
        else:
            buttons[row][column]["text"] = players[1]
            if check_winner() is False:
                player = players[0]
                theLabel.config(text= players[0] + " Turn")
            elif check_winner() is True:
                theLabel.config(text= players[1] + " Win!")
            elif check_winner() == "Tie":
                theLabel.config(text="Tie!")
   
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True    
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True        
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True        
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"    
    else:
        return False
            
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
    
def new_game():
    global players
    player = random.choice(players)
    theLabel.config(text=player+" Turn")
    
    for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="",bg="black")
    

window = Tk()
window.title("TicTacToe")
window.config(bg="black")
window.resizable(0,0)
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

theLabel = Label(text=player + " Turn", font=("arial",40))
theLabel.pack(side="top")
theLabel.config(bg="black",fg="red")

resetButton = Button(text="Restart", font=("arial", 20), bg="black", fg="red", command=new_game)
resetButton.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame , text="", bg="black", fg="red", font=("arial", 40), width=5, height=3, command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)


window.mainloop()