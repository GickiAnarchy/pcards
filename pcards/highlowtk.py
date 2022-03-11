#tkcards.py
import tkinter as tk
from PIL import Image, ImageTk 
import playingcards
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
        self.back = Card.getBackImage()
        self.playing = False
        self.frame = tk.Frame(self, width = 601, height = 500)
        self.frame.pack(fill = None, expand = False)
        self.tv = tk.StringVar()
        self.cd = None
        self.tv.set(repr(self.cd))
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
        self.c1 = tk.Label(self.frame, image = self.back)
        self.c1.grid(row = 0, column = 0)
        


    def drawc(self):
        self.cleft.set(self.deck.left)
        self.cd = self.deck.drawCard()
        self.tv.set("Card Drawn")
        self.c1.configure(image = self.back)
        self.c1.image = self.back

    def showc(self):
        self.tv.set(repr(self.cd))
        self.c1img = ImageTk.PhotoImage(Image.open(self.cd.imagePath()))
        #resize_image = c1img.resize((200, 340) , Image.ANTIALIAS)
        #img = ImageTk.PhotoImage(resize_image)
        self.imgs[repr(self.cd)] = self.c1img
        self.c1.configure(image = self.c1img)
        self.c1.image = self.c1img
        


if __name__ == "__main__":
    hl = highlowTk()
    hl.mainloop()
