from tkinter import *
from tkinter import messagebox


turn  = True  #For first person turn.
flag  = 1
empty = ' '
texts = ('O', 'X')
board = []


def on_click(row, column):
    global turn, flag
    board[row][column]['text'] = texts[turn]
    already_clicked.append((row, column))
    flag += 1
    turn = not turn
    check()


def check():
    global flag
    
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
        window.destroy()

    for r in range(3):
        if (board[r][0]['text'] ==\
            board[r][1]['text'] ==\
            board[r][2]['text'] != empty):
            win(board[r][0]['text'])
            return

    for c in range(3):
        if (board[0][c]['text'] ==\
            board[1][c]['text'] ==\
            board[2][c]['text'] != empty):
            win(board[0][c]['text'])
            return

    if (board[0][0]['text'] ==\
        board[1][1]['text'] ==\
        board[2][2]['text'] != empty):
        win(board[0][0]['text'])
        return

    if (board[0][2]['text'] ==\
        board[1][1]['text'] ==\
        board[2][0]['text'] != empty):
        win(board[0][2]['text'])
        return


def win(player):
    ans = "Game complete " + player + " wins!";
    messagebox.showinfo("Congratulations", ans)
    window.destroy()


window = Tk()
window.title("Welcome to The Gaming world TIC-Tac-Toe ")
window.geometry("400x300")

Label(window,text="Tic-tac-toe Game",font=('Helvetica','15')).grid(row=0,column=0)
Label(window,text="Player 1: X",font=('Helvetica','10')).grid(row=1,column=0)
Label(window,text="Player 2: O",font=('Helvetica','10')).grid(row=2,column=0)


for r in range(3):
    array = []
    for c in range(3):
        button = Button(master=window, text=empty, bg="yellow", fg="Black",
                        width=3, height=1, font=('Helvetica','20'),
                        command=lambda r=r, c=c: on_click(r, c))
        button.grid(row=r, column=c+1)
        array.append(button)
    board.append(array)


window.mainloop()
