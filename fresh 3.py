import tkinter as tk    
import fnmatch
import os
from pygame import mixer

canvas =tk.Tk()
canvas.title("music player")
canvas.geometry("600x400")
canvas.config(bg = "black")
rootpath = "c:\\songs"
pattern ="*.mp3"

mixer.init()


prev_img = tk.PhotoImage(file="C:\\Users\\hp\\Downloads\\backword image (1).png")
stop_img = tk.PhotoImage(file="C:\\Users\\hp\\Downloads\\stop button.png")
play_img = tk.PhotoImage(file="C:\\Users\\hp\\Downloads\\play button.png") 
pause_img = tk.PhotoImage(file="C:\\Users\\hp\\Downloads\\pause button.png")
next_img = tk.PhotoImage(file="C:\\Users\\hp\\Downloads\\forward button.png")      

def select():
    Label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))  
    mixer.music.play()
def stop():
    mixer.music.stop()
    listbox.select_clear("active")
def play_next():
    next_song = listbox.curselection()    
    next_song =next_song[0]+1
    next_song_name = listbox.get(next_song)
    Label.config(text = next_song_name)
    
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    
    listbox.select_clear(0, "end")
    listbox.activate(next_song)
    listbox.select_set(next_song)
    
def play_prev():
    next_song = listbox.curselection()    
    next_song =next_song[0]-1
    next_song_name = listbox.get(next_song)
    Label.config(text = next_song_name)
    
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    
    listbox.select_clear(0, "end")
    listbox.activate(next_song)
    listbox.select_set(next_song)   

def pause_song():
    if pausebutton["text"]== "pause":
        mixer.music.pause()
        pausebutton["text"]="play"
    else:
        mixer.music.unpause()
        pausebutton["text"]="pause"
        


listbox = tk.Listbox(canvas, fg= "cyan" , bg="black" , width = 100, font = ("poppins", 14))
listbox.pack(padx = 15, pady =15)

Label = tk.Label(canvas, text = "", bg = "black" , fg = "yellow" , font = ("poppins", 18))
Label.pack(pady = 15)

top = tk.Frame(canvas, bg="black")
top.pack(padx =10, pady =5, anchor="center")

prevbutton = tk.Button(canvas, text = "prev", image = prev_img, bg="black", borderwidth=0, command=play_prev)
prevbutton.pack(pady=15, in_ =top, side = "left")

stopbutton = tk.Button(canvas, text ="stop",image = stop_img, bg="black", borderwidth=0, command = stop) 
stopbutton.pack(pady= 15, in_=top,side ="left")

playbutton = tk.Button(canvas, text ="play",image = play_img, bg="black", borderwidth=0, command=select) 
playbutton.pack(pady= 15, in_=top,side ="left")


pausebutton = tk.Button(canvas, text ="pause",image = pause_img, bg="black", borderwidth=0,command=pause_song ) 
pausebutton.pack(pady= 15, in_=top,side ="left")

nextbutton = tk.Button(canvas, text ="next",image = next_img, bg="black", borderwidth=0, command=play_next) 
nextbutton.pack(pady= 15, in_=top,side ="left")


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listbox.insert("end", filename)
canvas.mainloop()