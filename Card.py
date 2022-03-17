class Card:
    index_to_rank={0:"A", 1:"K", 2:"Q", 3:"J", 4:"T", 5:"9", 6:"8", 7:"7", 8:"6", 9:"5", 10:"4", 11: "3", 12:"2"}
    index_to_suit={0:"Spades", 1:"Hearts", 2:"Diamonds", 3:"Clubs"}
    def __init__(self, index):
        #Card Deck will go like: 
        #0=Ace of Spades, 1=Ace of Hearts... 51=2 of clubs
        self.rank= Card.index_to_rank[int(index/4)]
        self.suit= Card.index_to_suit[index%4]
    def __repr__(self):
        return "{rank} of {suit}".format(rank=self.rank, suit=self.suit)
card1=Card(41)
print(card1)

