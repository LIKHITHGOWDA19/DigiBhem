import tkinter as gui
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")


        pygame.init()


        self.play_button = gui.Button(master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = gui.Button(master, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.stop_button = gui.Button(master, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.open_button = gui.Button(master, text="Open", command=self.open_file)
        self.open_button.pack(pady=10)


        pygame.mixer.init()

    def play_music(self):
        pygame.mixer.music.unpause()

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

if __name__ == "__main__":
    root = gui.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

