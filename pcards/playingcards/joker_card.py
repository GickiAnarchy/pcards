#joker_card.py
from cards import Card

class Joker(Card):
    """The Joker card which can have many unique rules according to the game."""
    
    def __init__(self, col):
        """col is either red or"""
        self.suit = 4
        if col == "red":
            self.value = 16
        elif col == "black":
            self.value = 17
        

    def __repr__(self):
        """Returns a string format of the object"""
        if self.value == 16:
            self.color = "Red"
        else:
            self.color = "Black"

        return f"{self.color} Joker"