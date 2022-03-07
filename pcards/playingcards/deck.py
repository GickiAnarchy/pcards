#deck.py
from joker_card import Joker

class Deck:
    """ Class of 52 Card() to create a full deck."""
    def __init__(self):
        self.cards = []
    
    def createDeck(self):
        for i in range(2, 15):
            for j in range(4):
                crd = Card(i, j)
                self.cards.append(crd)
        self.shuffle()
        
    def createDeckWithJokers(self):
        self.createDeck()
        redjr = Joker("red")
        blackjr = Joker("black")
        self.cards.append(redj)
        self.card.append(blackj)
        self.shuffle()
        
    def shuffle(self):
        if len(self.cards) == 0:
            return
        shuffle(self.cards)
        print(f"Shuffling {str(len(self.cards))} cards..")

    def drawCard(self):
        if len(self.cards) == 0:
            return
        pulled = self.cards.pop()
        print(f"Pulled card:\n{pulled}")
        return
    
    def drawHand(self, amount):
        self.hand = []
        while amount > 0:
            self.hand.append(self.drawCard())
        print(f"Dealt a hand of {str(amount)} cards")
        return self.hand
    
    