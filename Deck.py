from Card import Card
import random
class Deck:
    def __init__(self, ind1, ind2, ind3, ind4, ind5):
        self.card1=Card(ind1)
        self.card2=Card(ind2)
        self.card3=Card(ind3)
        self.card4=Card(ind4)
        self.card5=Card(ind5)
    def __repr__(self):
        return self.card1.__repr__()+self.card2.__repr__()+self.card3.__repr__()+self.card4.__repr__()+self.card5.__repr__()
    def ordered_deck(self):
        indices=[self.card1.card_to_index(), self.card2.card_to_index(), self.card3.card_to_index(), self.card4.card_to_index(), self.card5.card_to_index()]
        ordered_indices=sorted(indices)
        return Deck(ordered_indices[0],ordered_indices[1],ordered_indices[2],ordered_indices[3],ordered_indices[4])


deck=Deck(34, 35, 20, 1, 15)
print(deck)
deck2=deck.ordered_deck()
print(deck2)