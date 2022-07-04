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
                song_detail=(music.title,music.artist,music.album,music.genre,music.duration)
                if i%2==0:
                    playlist.insert(parent='',index=END,values=song_detail,tags=('even',))
                else:
                    playlist.insert(parent='',index=END,values=song_detail,tags=('odd',))
                i+=1

#------------------------------- Function to play song ------------------------------------
def play_song():
    global paused
    mixer.init()
    mixer.music.load(playlist.get(ACTIVE))  
    mixer.music.play()

#------------------------------ Initializing window for program -------------------------
mp=Tk()
mp.iconbitmap(r'rickroll.ico')
mp.title("ANA Music Player")
mp.config(bg='#0F111A')
mp.resizable(False,False)
# mp.geometry("1100x600")
mp.attributes("-fullscreen",True)

#------ Creating a black area in the bottom of window, where the commands will be shown ---------
bottom=Label(height='50',width='1100',bg='black').place(x=0,y=720)

#----------------------------- Creating buttons -----------------------------------
previous_button=PhotoImage(file="previous.png")
previous=Button(mp,image=previous_button,bd=0,bg='black',activebackground='black').place(x=40,y=740)

play_button=PhotoImage(file="play.png")
pause_button=PhotoImage(file="pause.png")

status=0
def pause_resume():
    mixer.init()
    global status,paused
    if status==0:
        play_song()
        play.config(image=pause_button,bd=0,bg='black',activebackground='black')
        status=1
    elif status==1:
        mixer.music.pause()
        play.config(image=play_button,bd=0,bg='black',activebackground='black')
        status=0

play=Button(mp,image=play_button,bd=0,bg='black',activebackground='black',command=pause_resume)
play.place(x=110,y=738)

next_button=PhotoImage(file="next.png")
next=Button(mp,image=next_button,bd=0,bg='black',activebackground='black',)
next.place(x=180,y=740)

#------------------ Title bar, to add commands like add song -----------------------

title_bar=Label(mp,bg='#040508',height='2',width='400').pack(side=TOP)
add_song=Button(mp,text='Add Songs',font=('Segoe',14,'bold'),fg='white',bg='#040508',bd=0,activebackground='#212942',activeforeground='#818182',command=open_folder).place(x=10,y=2)

#------------------ Created tree to display song details -------------------------
playlist=ttk.Treeview(mp,show='headings',height=19)
playlist["columns"]=('Title','Artist','Album','Genre','Time')

playlist.column('#0',width=0,stretch=NO)
playlist.column('Title',anchor=W,width=200,minwidth=50)
playlist.column('Artist',anchor=W,width=200,minwidth=50)
playlist.column('Album',anchor=W,width=200,minwidth=50)
playlist.column('Genre',anchor=W,width=150,minwidth=50)
playlist.column('Time',anchor=W,width=82,minwidth=50)

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
style.configure('Treeview',rowheight=25)
playlist.tag_configure('even',background='#737373',foreground='white')
playlist.tag_configure('odd',background='#4D4D4D',foreground='white')



mp.mainloop()
