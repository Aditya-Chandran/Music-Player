import tkinter as tk
from tkinter import *
from turtle import color

mp=Tk()
mp.iconbitmap(r'rickroll.ico')
mp.title("ANA Music Player")
mp.config(bg='#0F111A')
mp.geometry("600x400")
mp.resizable(False,False)

previous_button=PhotoImage(file="previous.png")
previous=Button(mp,image=previous_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=90,y=320)

play_button=PhotoImage(file="play.png")
active_play=PhotoImage(file="play_coloured.png")
play=Button(mp,image=play_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=210,y=320)

pause_button=PhotoImage(file="pause.png")
pause=Button(mp,image=pause_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=320,y=320)

next_button=PhotoImage(file="next.png")
next=Button(mp,image=next_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=440,y=320)

mp.mainloop()