#Highcard.py
#To replace highlowtk.py
import tkinter as tk
from PIL import Image, ImageTk 
from playingcards import *
import time


class Highcard(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("High Card")
        self.geometry("600x960")
        self.resizable(False, False)
        self.deck = Deck()
        self.deck.createDeck()
        self.playing = False
        
        self.frame = tk.Frame(self, width = 200, height = 360)
        self.frame.pack(fill = None, expand = False)
        
        self.back = Card.getBackImage()
        
        self.winner = tk.StringVar()
        self.winner.set("---")
        
        self.player_card = tk.Label(self.frame, image = self.back)
        self.dealer_card = tk.Label(self.frame, image = self.back)
        self.middle = tk.Label(self.frame, textvariable = self.winner).grid(row = 0, column = 1, sticky = tk.N)
        self.dealer_card.grid(row = 0, column = 0, sticky = tk.NW)
        self.player_card.grid(row = 0, column = 2, sticky = tk.NE)
        
        self.draw_button = tk.Button(self, text ="Draw Card", command=self.drawcrd)
        self.draw_button.pack(side=tk.BOTTOM, padx=(0, 20), pady=(0, 20))
        self.shuffle_button = tk.Button(self, text ="Shuffle Deck", command=self.shuffleDeck)
        self.shuffle_button.pack(side=tk.BOTTOM, padx=(0, 20), pady=(0, 20))



    def drawcrd(self):
        if self.deck.isEmpty:
            return
        self.dealerCard = self.deck.drawCard()
        imgd = self.dealerCard.Image
        self.dealer_card.configure(image = imgd)
        self.dealer_card.image = imgd
        self.playerCard = self.deck.drawCard()
        imgp = self.playerCard.Image
        self.player_card.configure(image = imgp)
        self.player_card.image = imgp
        self.checkWinner()
        
            
    def shuffleDeck(self):
        self.deck.Shuffle()
    
    def checkWinner(self):
        if self.dealerCard > self.playerCard:
            self.winner.set("Dealer Wins")
        else:
            self.winner.set("Player Wins")


if __name__ == "__main__":
    hl = highlowTk()
    hl.mainloop()
