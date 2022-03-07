#tkcards.py
from tkinter import *
from playingcards.cards import *
from playingcards.deck import *



deck = Deck()
deck.createDeck()
deck.shuffle()
window = Tk()

cardDraw: Card = deck.drawCard()

label = Label(image = cardDraw.loadImage()).pack



while True:
    window.mainloop()

