#tkcards.py
import tkinter as tk
from playingcards.cards import *
from playingcards.deck import *

imgs = []

deck = Deck()
deck.createDeck()
deck.Shuffle()
window = tk.Tk()
frame = tk.Frame(master = window)
frame.pack()

cardDraw = deck.drawCard()

image = Image.open(f"{cardDraw.imagepath}{cardDraw.imagename}")
resize_image = image.resize((300, 525) , Image.ANTIALIAS)
img = ImageTk.PhotoImage(resize_image)
imgs.append(img)
label1 = tk.Label(master = frame, image = img).pack()

label = tk.Label(master = frame, text = repr(cardDraw)).pack()

while True:
    window.mainloop()


