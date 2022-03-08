#cards.py
import os
import random
import tkinter
from PIL import Image, ImageTk



class Card:
    """Single playing card class"""

    imagepath = "images/"

    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, v):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.imagename = f"{self.suits[self.suit]}_{self.values[self.value]}.png"


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
    
    def imagePath(self):
        return f"{self.imagepath}{self.imagename}"
        
    @property
    def getImageName():
        return self.imagename        
