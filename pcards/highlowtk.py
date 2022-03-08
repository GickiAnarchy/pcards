#tkcards.py
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
        self.deck.Shuffle()
        self.playing = False
        self.tv = tk.StringVar()
        self.tv.set("....")
        self.lbl = tk.Label(self, textvariable = self.tv)
        self.lbl.pack(side=tk.TOP)
        self.cleft = tk.StringVar()
        self.cleft.set(self.deck.left)
        self.left = tk.Label(self, textvariable = self.cleft)
        self.left.pack()
        draw_button = tk.Button(self, text ="Draw Card", command=self.drawc)
        draw_button.pack(side=tk.BOTTOM, padx=(0, 20), pady=(0, 20))
        show_button = tk.Button(self, text ="Show Card", command=self.showc)
        show_button.pack(side=tk.BOTTOM, padx=(0, 20), pady=(0, 20))


    def drawc(self):
        self.cleft.set(self.deck.left)
        self.cd = self.deck.drawCard()
        self.tv.set("Card Drawn")

    def showc(self):
        self.tv.set(repr(self.cd))


if __name__ == "__main__":
    hl = highlowTk()
    hl.mainloop()