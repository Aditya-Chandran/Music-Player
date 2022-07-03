import tkinter as tk
from tkinter import *
from tkinter import filedialog
from turtle import color
import os
from pygame import mixer

def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    mixer.init()
    mixer.music.load(playlist.get(ACTIVE))  
    mixer.music.play()

mp=Tk()
mp.iconbitmap(r'rickroll.ico')
mp.title("ANA Music Player")
mp.config(bg='#0F111A')
mp.geometry("600x400")
mp.resizable(False,False)

previous_button=PhotoImage(file="previous_new.png")
previous=Button(mp,image=previous_button,bd=0,bg='#0F111A',activebackground='#0F111A',height=60,width=60).place(x=90,y=320)

play_button=PhotoImage(file="play_new.png")
play=Button(mp,image=play_button,bd=0,bg='#0F111A',activebackground='#0F111A',command=play_song,height=60,width=60).place(x=210,y=320)

pause_button=PhotoImage(file="pause_new.png")
pause=Button(mp,image=pause_button,bd=0,bg='#0F111A',activebackground='#0F111A',command=mixer.music.pause,height=60,width=60).place(x=320,y=320)

next_button=PhotoImage(file="next_new.png")
next=Button(mp,image=next_button,bd=0,bg='#0F111A',activebackground='#0F111A',height=60,width=60).place(x=440,y=320)

title_bar=Label(mp,bg='#040508',height='2',width='400').pack(side=TOP)
add_song=Button(mp,text='Add Songs',font=('Segoe',14,'bold'),fg='black',bg='#8904b5',bd=0,activebackground='#8904b5',activeforeground='black',command=open_folder).place(x=10,y=2)

music_list=Frame(mp,bd=2,relief=RIDGE)
music_list.place(x=150,y=100,width=350,height=200)

scroll=Scrollbar(music_list)

playlist=Listbox(music_list,width=350,font=("Candara",10),bg='black',fg='white',selectbackground='blue',bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

mp.mainloop()
