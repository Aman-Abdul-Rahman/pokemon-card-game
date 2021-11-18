# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:39:07 2021

@author: mx
"""

from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Pokemon card game")
root.geometry("900x900")
root.configure(background="yellow")

pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))


player1=Label(root,text="player 1", bg="red",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="player 2", bg="red",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player_score1=Label(root,bg="red",fg="white")
player_score1.place(relx=0.1,rely=0.4,anchor=CENTER)

player_score2=Label(root,bg="red",fg="white")
player_score2.place(relx=0.9,rely=0.4,anchor=CENTER)

canvas = Canvas(root, width = 400, height = 500)
canvas.pack()

canvas.create_image(20, 20, anchor=NW, image=pikachu)

root.mainloop()