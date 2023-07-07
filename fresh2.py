from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.title('jaya.com mp player')


#initialize pygame mixer
pygame.mixer.init()

#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir= "audio/" , title="choose a song", filetypes=(("mp3 files","*.mp3"),))
    
    #strip out the directory info and .mp3extension from the song name
    song =song.replace("C:\\gui\\audio\\", "")
    
    song =song.replace(".mp3", "")
    
    #add songto listbox
    
    song_box.insert(END, song)
#add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir= "audio/" , title="choose a song", filetypes=(("mp3 files","*.mp3"),))
    #loop through song list and replace directory info and mp3
    for song in songs:
        song =song.replace("C:\\gui\\audio\\", "")
    
        song =song.replace(".mp3", "")
        #insert into playlist
        song_box.insert(END, song)
        
#play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f"C:\\gui\\audio\\"
    pygame.mixer.music.load(song)
    
     

    
    pygame.mixer.music.play(loops=0)
    
#stop playing current song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
#create global paused variable
global paused
paused=False
    
#pause and unpause the current song

def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        #unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        #pause
        pygame.mixer.music.pause()
        paused = True
    
    
    
    
#create playlist box
song_box = Listbox(root, bg="black", fg="green", width=60 , selectbackground="gray", selectforeground="black")
song_box.pack(pady=20)
# define player control buttons images
back_btn_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\backword image (1).png")
forward_btn_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\forward button.png")
play_btn_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\play button.png") 
pause_btn_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\pause button.png")
stop_btn_img = PhotoImage(file="C:\\Users\\hp\\Downloads\\stop button.png")

#create player control frame
controls_frame = Frame(root)
controls_frame.pack()

#create player control buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0 , padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)
# create add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_song)

#add many song to playlist
add_song_menu.add_command(label="Add many songs  to playlist", command=add_many_songs)





root.mainloop()