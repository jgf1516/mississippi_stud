class Card:
    index_to_rank={0:"A", 1:"K", 2:"Q", 3:"J", 4:"T", 5:"9", 6:"8", 7:"7", 8:"6", 9:"5", 10:"4", 11: "3", 12:"2"}
    index_to_suit={0:"Spades", 1:"Hearts", 2:"Diamonds", 3:"Clubs"}
    def __init__(self, index):
        #Card Deck will go like: 
        #0=Ace of Spades, 1=Ace of Hearts... 51=2 of clubs
        self.rank= Card.index_to_rank[int(index/4)]
        self.suit= Card.index_to_suit[index%4]
    def __repr__(self):
        #First, find corresponding suit unicode
        self.suit_char=""
        if self.suit=="Spades":
            self.suit_char="\u2660"
        elif self.suit=="Hearts":
            self.suit_char="\u2661"
        elif self.suit=="Diamonds":
            self.suit_char="\u2662"
        else:
            self.suit_char="\u2663"
        #Then print the rank, then the suit, then a space
        return "{rank}{suit} ".format(rank=self.rank, suit=self.suit_char)
    def card_to_index(self):
        ri=0
        si=0
        for r in Card.index_to_rank:
            if Card.index_to_rank[r]==self.rank:
                ri=r
                break
        for s in Card.index_to_suit:
            if Card.index_to_suit[s]==self.suit:
                si=s
                break
        return int(4 * ri + si)
#some testing:
#card1=Card(40)
#print(card1)
#print(card1.card_to_index())

