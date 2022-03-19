from Card import Card
from Deck import Deck
import random

#Set payouts:
#This multiplies wager amount returned, thus a loss is 0, a push is 1, 1 to 1 is 2, etc. Should be x+1 where payout is x to 1
payout_table={"No hand": 0, "6's through T's": 1, "Jacks or better": 2, "Two pair": 3, "Three of a kind": 4, "Straight": 5, "Flush": 7, "Full house": 11, "Four of a kind": 41, "Straight flush": 101, "Royal flush": 501}