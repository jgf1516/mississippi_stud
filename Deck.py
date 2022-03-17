import Card
import random
class Deck:
    def __init__(self, ind1, ind2, ind3, ind4, ind5):
        self.card1=Card(ind1)
        self.card2=Card(ind2)
        self.card3=Card(ind3)
        self.card4=Card(ind4)
        self.card5=Card(ind5)