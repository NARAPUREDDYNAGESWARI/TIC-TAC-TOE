import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self):
        self.currentplayer="x"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("TicTacToe")
        self.button=[]
        for i in range(3):
            rows=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=20,height=10,command=lambda i=i,j=j: self.makemove(i,j))
                button.grid(row=i,column=j)
                rows.append(button)
            self.button.append(rows)
    def makemove(self,row,col):
          if self.board[row][col]=="":
              self.board[row][col]=self.currentplayer
              self.button[row][col].config(text=self.currentplayer)
              if self.checkwinner(self.currentplayer):
                  messagebox.showinfo("gameover","The winner is" + self.currentplayer)
                  self.window.quit()
              elif self.isdraw():
                  messagebox.showinfo("gameover","its a draw")
                  self.window.quit()
              else:
                  self.currentplayer="o" if self.currentplayer=="x" else "x"
    def checkwinner(self,player):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]==player:
                return True
            if self.board[0][i]==self.board[1][i]==self.board[2][i]==player:
                return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2]==player:
            return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0]==player:
            return True
        return False
    def isdraw(self):
        for row in self.board:
            if "" in row:
                return False
            return True
    def run(self):
        self.window.mainloop()
game=TicTacToe()
game.run()
