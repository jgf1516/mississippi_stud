from Card import Card
import random
class Deck:

#This Deck class is specifically designed to create a 5 card poker hand for mississippi stud
#This could be reused in other card games
#I might later update this to make it more generalized as it could be useful in other card games

    hands={0: "No hand", 1: "6's through T's", 2: "Jacks or better", 3: "Two pair", 4: "Three of a kind", 5: "Straight", 6: "Flush", 7: "Full house", 8: "Four of a kind", 9: "Straight flush", 10: "Royal flush"}
    def __init__(self, ind1, ind2, ind3, ind4, ind5):
        self.card1=Card(ind1)
        self.card2=Card(ind2)
        self.card3=Card(ind3)
        self.card4=Card(ind4)
        self.card5=Card(ind5)
    
    def shuffled_deck(self):
        indices=list(range(0,52))
        ind1=indices.pop(random.randint(0,len(indices)-1))
        ind2=indices.pop(random.randint(0,len(indices)-1))
        ind3=indices.pop(random.randint(0,len(indices)-1))
        ind4=indices.pop(random.randint(0,len(indices)-1))
        ind5=indices.pop(random.randint(0,len(indices)-1))
        return Deck(ind1, ind2, ind3, ind4, ind5)
        
    def __repr__(self):
        return self.card1.__repr__()+self.card2.__repr__()+self.card3.__repr__()+self.card4.__repr__()+self.card5.__repr__()

    def show_cards(self, number):
        out=""
        if number>=1:
            out+=self.card1.__repr__()
        if number>=2:
            out+=self.card2.__repr__()
        if number>=3:
            out+=self.card3.__repr__()
        if number>=4:
            out+=self.card4.__repr__()
        if number>=5:
            out+=self.card5.__repr__()
        print(out)
        return out

    def ordered_deck(self):
        indices=[self.card1.card_to_index(), self.card2.card_to_index(), self.card3.card_to_index(), self.card4.card_to_index(), self.card5.card_to_index()]
        ordered_indices=sorted(indices)
        return Deck(ordered_indices[0],ordered_indices[1],ordered_indices[2],ordered_indices[3],ordered_indices[4])

#This will find the hand of the 5 card deck.
#This is much simpler to do with an ordered deck
#This will output an integer representing the hand
#This integer will be the key for Deck.hands dict
    def find_hand(self):
        #For now, since I anticipate reusing deck d many times, I will simply call it d for now, may change later
        d=self.ordered_deck()
      
        isFlush = d.card1.suit==d.card2.suit==d.card3.suit==d.card4.suit==d.card5.suit
        
        #I know this is a lot for one line, the or condition is to check for A-5 straights
        isStraight = (d.card1.rank_to_rank_index()+4==d.card2.rank_to_rank_index()+3==d.card3.rank_to_rank_index()+2==d.card4.rank_to_rank_index()+1==d.card5.rank_to_rank_index()) or (d.card1.rank=="A" and d.card2.rank=="5" and d.card3.rank=="4" and d.card4.rank=="3" and d.card5.rank=="2")
        

        #Check Royal
        if isStraight and isFlush:
            if d.card1.rank=="A" and d.card2.rank=="K":
                return 10
        #Check Straight Flush
            else:
                return 9
        
        #Check 4 of a kind
        if (d.card1.rank==d.card4.rank) or (d.card2.rank==d.card5.rank):
            return 8

        #Check full house
        if (d.card1.rank==d.card3.rank and d.card4.rank==d.card5.rank) or (d.card1.rank==d.card2.rank and d.card3.rank==d.card5.rank):
            return 7

        #Check flush
        if isFlush:
            return 6

        #Check straight
        if isStraight:
            return 5

        #Check 3 of a kind
        if (d.card1.rank==d.card3.rank) or (d.card2.rank==d.card4.rank) or (d.card3.rank==d.card5.rank):
            return 4

        #Check 2 pair
        if (d.card1.rank==d.card2.rank and (d.card3.rank==d.card4.rank or d.card4.rank==d.card5.rank)) or (d.card2.rank==d.card3.rank and d.card4.rank==d.card5.rank):
            return 3

        #Check jacks or better
        if (d.card1.rank==d.card2.rank and d.card2.rank_to_rank_index()<=3) or (d.card2.rank==d.card3.rank and d.card3.rank_to_rank_index()<=3) or (d.card3.rank==d.card4.rank and d.card4.rank_to_rank_index()<=3) or (d.card4.rank==d.card5.rank and d.card5.rank_to_rank_index()<=3):
            return 2

        #Check 6's thru 10's
        if (d.card1.rank==d.card2.rank and d.card2.rank_to_rank_index()<=8) or (d.card2.rank==d.card3.rank and d.card3.rank_to_rank_index()<=8) or (d.card3.rank==d.card4.rank and d.card4.rank_to_rank_index()<=8) or (d.card4.rank==d.card5.rank and d.card5.rank_to_rank_index()<=8):
            return 1

        return 0
        
    
#


