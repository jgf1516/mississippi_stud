from Card import Card
from Deck import Deck
import random
class Game:
    #Set payouts:
    #This multiplies wager amount returned, thus a loss is 0, a push is 1, 1 to 1 is 2, etc. Should be x+1 where payout is x to 1
    payout_table={"No hand": 0, "6's through T's": 1, "Jacks or better": 2, "Two pair": 3, "Three of a kind": 4, "Straight": 5, "Flush": 7, "Full house": 11, "Four of a kind": 41, "Straight flush": 101, "Royal flush": 501}

    def __init__(self, balance=10000, wager_size=100):
        self.wager_size=wager_size
        self.balance=balance


    def help_menu(self):
        print("\tW: make a wager")
        print("\tC: adjust wager size")
        print("\tP: adjust pay table")
        print("\tB: view current balance")
        print("\tH: view help menut")
        print("\tX: exit")


    def accept_menu_choice(self):
        self.help_menu()
        menu_choice=input("Make selection: ")
        if menu_choice.upper()=="W":
            #This is where the game will be played
            self.play_round(self.balance, self.wager_size)
        elif menu_choice.upper()=="C":
            #adjust wager size
            self.adjust_wager_size()

    def play_round(self):
    #This will be where the logic of the game is defined
    #When a wager is accepted, that wager will be deducted from the balance
    #Then a new shuffled Deck is created, which will have a hand value
    #If the player makes it to the end of the hand, the wager will be multiplied
    #by the corresponding amount from the payout table times the total number of chips (1-10 wager amounts)
    #First: 2 cards are revealed, player can fold(0), bet 1x, bet 2x or bet 3x
    #Second: one more card is revealed, player bets up to 3x or fold again
    #Third: one more card is revealed, player makes one last 1-3x bet or fold
    #The final card is revealed, hand is printed, winnings calculated, printed, and added to balance
    #then back to the menu

        pass

    def adjust_wager_size(self):
        print("Current wager size is ${amount}".format(amount=self.wager_size))
        wager_in_a=input("Enter wager: $")
        try:
            wager_in=int(wager_in_a)
            if 1<=wager_in<=int(self.balance/10):
                self.wager_size=int(wager_in)
                return wager_in
            else:
                print("Wager can be no more than $" + str(int(self.balance/10))+" (i.e. one-tenth of your balance)")
                self.adjust_wager_size()
        except ValueError:
            print("Wager must be an integer")
            self.adjust_wager_size()
 

game = Game()
print("Welcome to Mississippi Stud!")
game.accept_menu_choice()
print(game.wager_size)
