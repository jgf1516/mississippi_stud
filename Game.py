from Card import Card
from Deck import Deck
import random
class Game:
    #Set payouts:
    #This multiplies wager amount returned, thus a loss is 0, a push is 1, 1 to 1 is 2, etc. Should be x+1 where payout is x to 1
    payout_table={"No hand": 0, "6's through T's": 1, "Jacks or better": 2, "Two pair": 3, "Three of a kind": 4, "Straight": 5, "Flush": 7, "Full house": 11, "Four of a kind": 41, "Straight flush": 101, "Royal flush": 501}
    quit=False

    def __init__(self, balance=10000, wager_size=100):
        self.wager_size=wager_size
        self.balance=balance


    def help_menu(self):
        print("Menu: ")
        print("\tENTER: Make a Wager")
        print("\tC: Adjust Wager Size")
        print("\tB: View Current Balance")
        print("\tP: View Payout Table")
        print("\tH: How to Play")
        print("\tX: exit")



    def accept_menu_choice(self):
        self.help_menu()
        menu_choice=input("Make selection: ")
        if menu_choice.upper()=="":
            #This is where the game will be played
            self.play_round()

        elif menu_choice.upper()=="B":
            #show balance
            self.view_balance()

        elif menu_choice.upper()=="C":
            #adjust wager size
            self.adjust_wager_size()

        elif menu_choice.upper()=="H":
            #how to play
            self.how_to_play()

        elif menu_choice.upper()=="X":
            #quit game
            self.quit_game()
        
        elif menu_choice.upper()=="P":
            #show payouts
            self.view_payout_table()

        else:
            print("Invalid selection. Please type the letter that corresponds to your choice, then press ENTER")


    def quit_game(self):
        #Exit game
        print("Thank you for playing! Good bye")
        Game.quit=True


    def view_balance(self):
        print("Your balance is: ${balance}".format(balance=self.balance))
        return self.balance

    def view_payout_table(self):
        for i in Game.payout_table:
            if i=="No hand":
                print(i+ ": \n\tLose")
            elif i=="6's through T's":
                print(i+ ": \n\tPush")
            else:
                print(i + ": \n\t" + str(Game.payout_table[i]-1)+ ":1")

    def how_to_play(self):
        print("Mississippi Stud:")
        print("\tYour goal is to make a hand, which will pay out according to the payout table")
        print("\t(enter P in the menu to see payouts)")
        print("\tTo play, make an initial wager")
        print("\tYou will then be dealt 2 cards")
        print("\tYou can now fold (forfeit the hand), or increase your bet by 1, 2, or 3 times your initial wager")
        print("\tYou will then be dealt a third card")
        print("\tOnce again you may fold, or bet an additional 1-3x")
        print("\tYou will be dealt a 4th card")
        print("\tOne last time, you may fold or bet 1-3x")
        print("\tYour 5th and final card will now be revealed")
        print("\tYour winnings (or lack thereof) are then paid out based on your hand and total wager")


    def adjust_wager_size(self):
        print("Current wager size is ${amount}".format(amount=self.wager_size))
        wager_in_a=input("Enter wager: $")
        try:
            wager_in=int(wager_in_a)
            if 1<=wager_in<=int(self.balance/10):
                self.wager_size=int(wager_in)
                print("New wager is: ${wager}".format(wager=self.wager_size))
                return wager_in
            else:
                print("Wager can be no more than $" + str(int(self.balance/10))+" (i.e. one-tenth of your balance)")
                self.adjust_wager_size()
        except ValueError:
            print("Wager must be an integer")
            self.adjust_wager_size()
 

    def get_bet(self):
        print("1- Bet 1x, 2- Bet 2x, 3- Bet3x, Anything else- Fold")
        bet=input("Bet: ")
        if bet=="1" or bet=="2" or bet=="3":
            return int(bet)
        else:
            return 0

    def street(self, deck, number, wager_mult):
        deck.show_cards(number)
        bet=self.get_bet()
        if bet==0:
            print("You fold")
            return 0
        else:
            wager_mult+=bet
            self.balance-=bet*self.wager_size
            self.view_balance()
            return bet


    def play_round(self):
        #This will be where the logic of the game is defined
        if self.balance<100:
            self.balance+=10000
            print("Your balance is getting low. Have an extra $10000 on us!")
        self.balance-=self.wager_size
        print("Your balance is ${balance}. You are wagering ${wager}.".format(balance=self.balance, wager=self.wager_size))
        wager_mult=1
        deck=Deck(1,2,3,4,5)
        deck=deck.shuffled_deck()

        #First 2 cards
        fold=self.street(deck, 2, wager_mult)
        if fold==0:
            return
        
        #3rd card
        fold=self.street(deck, 3, wager_mult)
        if fold==0:
            return

        #4th card
        fold=self.street(deck, 4, wager_mult)
        if fold==0:
            return

        #Reveal
        deck.show_cards(5)
        winnings=self.wager_size*wager_mult*Game.payout_table[Deck.hands[deck.find_hand()]]
        self.balance+=winnings
        print("You have: "+ Deck.hands[deck.find_hand()])
        print("You've won ${amount}".format(amount=winnings))
        self.view_balance()

            





