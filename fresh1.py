from tkinter import *
import pygame
root = Tk()
root.title("jaya.com")





pygame.mixer.init()
def play():
    pygame.mixer.music.load("C:\\Users\\hp\\Downloads\\Moon Rise(PagalWorld.com.se).mp3")
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()




my_button = Button(root, text="play song", font=("Helvetica",32), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="stop", command=stop)
stop_button.pack(pady=20)


root.mainloop()