#deck.py
from .joker_card import Joker
from .cards import Card
from random import shuffle
from PIL import Image, ImageTk

class Deck:
    """ Class of 52 Card() to create a full deck."""
    def __init__(self):
        self.cards = []
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
        if len(self.cards) <= 0:
            return
        pulled = self.cards.pop()
        print(f"Pulled card:\n{pulled}")
        return pulled


    @property
    def left(self):
        return str(len(self.cards))