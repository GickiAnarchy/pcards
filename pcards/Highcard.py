#Highcard.py
#To replace highlowtk.py
import tkinter as tk
from PIL import Image, ImageTk 
from playingcards import *
import time


class highcardTk(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("High Card")
        self.geometry("800x640")
        self.resizable(False, False)
        self.imgs = {}
        self.deck = Deck()
        self.deck.createDeck()
        self.playing = False




if __name__ == "__main__":
    hl = highlowTk()
    hl.mainloop()
