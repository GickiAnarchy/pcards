from .playingcards import * 

class Player():
    """    """
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.hand = Hand(dealer = self.dealer)


    @property
    def hand(self):
        return self.hand