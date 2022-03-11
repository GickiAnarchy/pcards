#cards.py
import os
import random
import tkinter as tk
from PIL import Image, ImageTk

image_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),"..", "images"))

class Card():
    """Single playing card class"""

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, v):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.name = f"{self.suits[self.suit]}_{self.values[self.value]}"
        self.imagename = f"{self.name}.png"


    def __lt__(self, c2):
        """Handles the 'less than' operator (<)"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
        else:
            return False
        return False

    def __gt__(self, c2):
        """Handles the 'greater than' operator (>)"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
         if self.suit > c2.suit:
            return True
        else:
            return False
        return False

    def __repr__(self):
        """Returns a string format of the object"""
        v = self.values[self.value] +\
        " of " + \
        self.suits[self.suit]
        return v

    @classmethod
    def getBackImage(cls):
        cback = Image.open(image_folder + "/back.png")
        resized = cback.resize((200, 360))
        cls.back = ImageTk.PhotoImage(resized)
        return cls.back


    def getImage(self):
        tkimage = Image.open(image_folder + f"/{self.imagename}")
        resized = tkimage.resize((200, 360))
        self.image = ImageTk.PhotoImage(resized)
    
    @property
    def Image(self):
        self.getImage()
        return self.image