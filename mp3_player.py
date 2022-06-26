import tkinter as tk
from tkinter import *
from turtle import color
from tkinter import filedialog
from turtle import color
import os

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        print(songs)
    
mp=Tk()
mp.iconbitmap(r'rickroll.ico')
mp.title("ANA Music Player")
mp.config(bg='#0F111A')
mp.geometry("960x540")
mp.resizable(False,False)

previous_button=PhotoImage(file="previous.png")
previous=Button(mp,image=previous_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=90,y=320)

play_button=PhotoImage(file="play.png")
play=Button(mp,image=play_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=210,y=320)

pause_button=PhotoImage(file="pause.png")
pause=Button(mp,image=pause_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=320,y=320)

next_button=PhotoImage(file="next.png")
next=Button(mp,image=next_button,bd=0,bg='#0F111A',activebackground='#0F111A').place(x=440,y=320)

title_bar=Label(mp,bg='#040508',height='2',width='400').pack(side=TOP)
add_song=Button(mp,text='Add Songs',font=('Segoe',14,'bold'),fg='white',bg='#040508',bd=0,activebackground='#212942',activeforeground='#818182',command=open_folder).place(x=10,y=2)

music_frame=Label(mp,height='15',width='66').place(x=100,y=70)
menu=Frame(mp,bd=1,relief=RIDGE,height='230.5',width='450',bg='#8182FF').place(x=100,y=70)

playlist=Listbox(music_frame,width=66,font=('Segoe',10),fg='white',bg='black',selectbackground='#2E3596',bd=0).pack(side=LEFT,fill=BOTH)
scroll=Scrollbar(music_frame,orient='vertical',command=playlist).pack(side=RIGHT,fill=Y)

mp.mainloop()
