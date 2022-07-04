import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Treeview
from turtle import color
import os
from pygame import mixer
from tinytag import TinyTag

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
                song_detail=(song_path,music.title,music.artist,music.album,music.genre,int(music.duration))
                if i%2==0:
                    playlist.insert(parent='',index=END,iid=i,values=song_detail,tags=('even',))
                else:
                    playlist.insert(parent='',index=END,iid=i,values=song_detail,tags=('odd',))
                i+=1

#------------------------------- Music control functions ------------------------------------
paused=True
selected=""
old_selection=""
def check():
    global selected,old_selection,paused
    selected=playlist.focus()
    paused=False
    if old_selection==selected:
        resume_song()
    else:
        play_song()

def resume_song():
    play.config(image=pause_button,command=pause_song)
    mixer.init()
    mixer.music.unpause()

def play_song():
    global selected,old_selection
    mixer.init()
    play.config(image=pause_button,command=pause_song)
    old_selection=selected
    values=playlist.item(selected,'values')
    path=values[0]
    mixer.music.load(path)
    mixer.music.play()

def pause_song():
    mixer.init()
    mixer.music.pause()
    play.config(image=play_button,command=check)
    

#------ Creating a black area in the bottom of window, where the commands will be shown ---------
bottom=Label(height='10',width='1100',bg='black').place(x=0,y=540)

#----------------------------- Creating buttons -----------------------------------
previous_button=PhotoImage(file="previous.png")
previous=Button(mp,image=previous_button,bd=0,bg='black',activebackground='black').place(x=40,y=555.5)

play_button=PhotoImage(file="play.png")
pause_button=PhotoImage(file="pause.png")

play=Button(mp,image=play_button,bd=0,bg='black',activebackground='black',command=check)
play.place(x=110,y=553)

next_button=PhotoImage(file="next.png")
next=Button(mp,image=next_button,bd=0,bg='black',activebackground='black',)
next.place(x=180,y=555.5)

#------------------ Title bar, to add commands like add song -----------------------

title_bar=Label(mp,bg='#040508',height='2',width='400').pack(side=TOP)
add_song=Button(mp,text='Add Songs',font=('Segoe',14,'bold'),fg='white',bg='#040508',bd=0,activebackground='#212942',activeforeground='#818182',command=open_folder).place(x=10,y=2)

#------------------ Created tree to display song details -------------------------
playlist=ttk.Treeview(mp,show='headings',height=19)
playlist["columns"]=('Path','Title','Artist','Album','Genre','Time')

playlist.column('#0',width=0,stretch=NO)
playlist.column('Path',width=0,stretch=NO)
playlist.column('Title',anchor=W,width=200,minwidth=50)
playlist.column('Artist',anchor=W,width=200,minwidth=50)
playlist.column('Album',anchor=W,width=200,minwidth=50)
playlist.column('Genre',anchor=W,width=150,minwidth=50)
playlist.column('Time',anchor=W,width=82,minwidth=50)

playlist.heading('Path',text='Path',anchor=W)
playlist.heading('Title',text='Title',anchor=W)
playlist.heading('Artist',text='Artist',anchor=W)
playlist.heading('Album',text='Album',anchor=W)
playlist.heading('Genre',text='Genre',anchor=W)
playlist.heading('Time',text='Time',anchor=W)

playlist.place(x=250,y=35)

scroll=ttk.Scrollbar(mp,orient=VERTICAL,command=playlist.yview)
playlist.configure(yscroll=scroll.set)
scroll.pack(side=RIGHT,fill=Y)

style=ttk.Style(mp)
style.theme_use("clam")
style.configure('Treeview',rowheight=25,fieldbackground='silver')
playlist.tag_configure('even',background='#737373',foreground='white')
playlist.tag_configure('odd',background='#4D4D4D',foreground='white')

mp.mainloop()
