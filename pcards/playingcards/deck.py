#deck.py
from .joker_card import Joker
from .cards import Card
from random import shuffle
from PIL import Image, ImageTk 

class Deck:
    """ Class of 52 Card() to create a full deck."""
    def __init__(self):
        self.cards = []
        self.heldcards = []
        self.images = []
        

    
    def createDeck(self):
        for i in range(2, 15):
            for j in range(4):
                crd = Card(j, i)
                self.cards.append(crd)
        self.Shuffle()
        
    def createDeckWithJokers(self):
        self.createDeck()
        redjr = Joker("red")
        blackjr = Joker("black")
        self.cards.append(redj)
        self.card.append(blackj)
        self.Shuffle()
        
    def Shuffle(self):
        if len(self.cards) == 0:
            return
        shuffle(self.cards)
        print(f"Shuffling {str(len(self.cards))} cards..")

    def drawCard(self):
        if len(self.heldcards) > 0:
            self.heldcards.clear()
            print("Removed old held cards.")
        if len(self.cards) == 0:
            return
        pulled = self.cards.pop()
        print(f"Pulled card:\n{pulled}")
        self.heldcards.append(pulled)
        return self.heldcards[0]
    
    def drawHand(self, amount):
        if len(self.heldcards) > 0:
            self.heldcards.clear()
            print("Removed old held cards.")
        while amount > 0:
            self.heldcards.append(self.drawCard())
        print(f"Dealt a hand of {str(amount)} cards")
        return self.heldcards
    
    @property
    def left(self):
        return str(len(self.cards))