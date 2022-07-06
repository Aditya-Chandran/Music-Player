import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Treeview
from turtle import color
import os
import pygame
from pygame import mixer
from tinytag import TinyTag
import time

#------------------------------ Initializing window for program -------------------------
mp=Tk()
mp.iconbitmap(r'rickroll.ico')
mp.title("ANA Music Player")
mp.config(bg='#0F111A')
mp.resizable(False,False)
mp.geometry("1100x600")

#-------------- this will open a dialogue box to select song folder ------------------------------
def open_folder():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        i=0
        for song in songs:
            if song.endswith(".mp3"):
                song_path=f"{path}/{song}"
                music=TinyTag.get(song_path)
                # changing the float time of song in hh : mm : ss form
                duration=''
                if music.duration>=3600:
                    duration=time.strftime('%H : %M : %S',time.gmtime(music.duration))
                else:
                    duration=time.strftime('%M : %S',time.gmtime(music.duration))
                song_detail=(song_path,music.title,music.artist,music.album,music.genre,duration)
                if i%2==0:
                    playlist.insert(parent='',index=END,iid=i,values=song_detail,tags=('even',))
                else:
                    playlist.insert(parent='',index=END,iid=i,values=song_detail,tags=('odd',))
                i+=1

#------------------------------- Music control functions ------------------------------------

paused=True
selected=""
old_selection=""
paused=False
length=0

#............... display length of the new song ..........
def change_length(values):
    global length
    length=values[5]
    length=length.split(" : ")
    sum,i=0,len(length)-1
    while i!=-1:
        if i==len(length)-1:
            sum+=int(length[i])
        else:
            sum+=int(length[i])*60
        i-=1
    length=sum

#......... checks if music is starting or was already playing ..........

def check():
    global selected,old_selection,paused
    selected=playlist.focus()
    paused=False
    if old_selection==selected:
        resume_song()
    else:
        play_song()

#.................. resume function ......................

def resume_song():
    play.config(image=pause_button,command=pause_song)
    mixer.init()
    mixer.music.unpause()

#.................... play new song function ....................
def play_song():
    global selected,old_selection
    mixer.init()
    play.config(image=pause_button,command=pause_song)
    old_selection=selected
    values=playlist.item(selected,'values')
    path=values[0]
    change_length(values)
    mixer.music.load(path)
    slider.config(to=length)
    mixer.music.play()

#................... pause song .............................

def pause_song():
    global paused
    mixer.init()
    mixer.music.pause()
    paused=True
    play.config(image=play_button,command=check)
    
#..................... plays next song ............................

def next_song():
    mixer.init()
    play.config(image=pause_button,command=pause_song)
    global selected,old_selection
    selected=str(int(selected)+1)
    old_selection=selected
    values=playlist.item(selected,'values')
    path=values[0]
    change_length(values)
    slider.config(to=length,value=0)
    mixer.music.load(path)
    mixer.music.play()

#..................... plays previous song ......................

def previous_song():
    play.config(image=pause_button,command=pause_song)
    mixer.init()
    global selected,old_selection
    selected=str(int(selected)-1)
    old_selection=selected
    values=playlist.item(selected,'values')
    path=values[0]
    change_length(values)
    slider.config(to=length,value=0)
    mixer.music.load(path)
    mixer.music.play()

#............ creating a label for all commands button ......................
bottom=Label(height='10',width='1100',bg='black').place(x=0,y=540)

#----------------------------- Creating buttons -----------------------------------
previous_button=PhotoImage(file="previous.png")
previous=Button(mp,image=previous_button,bd=0,bg='black',activebackground='black',command=previous_song)
previous.place(x=40,y=555.5)

play_button=PhotoImage(file="play.png")
pause_button=PhotoImage(file="pause.png")

play=Button(mp,image=play_button,bd=0,bg='black',activebackground='black',command=check)
play.place(x=110,y=553)

next_button=PhotoImage(file="next.png")
next=Button(mp,image=next_button,bd=0,bg='black',activebackground='black',command=next_song)
next.place(x=180,y=555.5)

#------------------ Title bar, to add commands like add song -----------------------

title_bar=Label(mp,bg='#040508',height='2',width='400').pack(side=TOP)
add_song=Button(mp,text='Add Songs',font=('Segoe',14,'bold'),fg='white',bg='#040508',bd=0,activebackground='#212942',activeforeground='#818182',command=open_folder).place(x=10,y=2)

#------------------ Created tree to display song details -------------------------
playlist=ttk.Treeview(mp,show='headings',height=19)
playlist["columns"]=('Path','Title','Artist','Album','Genre','Time')

#setting width of playlist columns
playlist.column('#0',width=0,stretch=NO)
playlist.column('Path',width=0,stretch=NO)
playlist.column('Title',anchor=W,width=200,minwidth=50)
playlist.column('Artist',anchor=W,width=200,minwidth=50)
playlist.column('Album',anchor=W,width=200,minwidth=50)
playlist.column('Genre',anchor=W,width=150,minwidth=50)
playlist.column('Time',anchor=E,width=82,minwidth=50)

#setting headings of playlist columns
playlist.heading('Path',text='Path',anchor=W)
playlist.heading('Title',text='Title',anchor=W)
playlist.heading('Artist',text='Artist',anchor=W)
playlist.heading('Album',text='Album',anchor=W)
playlist.heading('Genre',text='Genre',anchor=W)
playlist.heading('Time',text='Time',anchor=W)

playlist.place(x=250,y=35)

#adding a scrollbar to the playlist
scroll=ttk.Scrollbar(mp,orient=VERTICAL,command=playlist.yview)
playlist.configure(yscroll=scroll.set)
scroll.pack(side=RIGHT,fill=Y)

#changing style of the playlist
style=ttk.Style(mp)
style.theme_use("clam")
style.configure('Treeview',rowheight=25,fieldbackground='silver')
playlist.tag_configure('even',background='#737373',foreground='white')
playlist.tag_configure('odd',background='#4D4D4D',foreground='white')

#------------------------- Making slider ------------------------------------
slider_timer=Label(mp,text='- / -',bg='black',fg='white')
slider_timer.place(x=760,y=540)

slider=ttk.Scale(mp,from_=0,orient=HORIZONTAL,value=0,length=600)
slider.place(x=250,y=565)

song_name=Label(mp,bg='black',fg='white')
song_name.place(x=246,y=540)




mp.mainloop()
