import random

#starts a new game after each hand

while True:

    #allows player to hit

    playerIn=True

    #deck of cards
     
    deck=[2,3,4,5,6,7,8,9,10,"A","J","K","Q",
    2,3,4,5,6,7,8,9,10,"A","J","K","Q",
    2,3,4,5,6,7,8,9,10,"A","J","K","Q",
    2,3,4,5,6,7,8,9,10,"A","J","K","Q",
    2,3,4,5,6,7,8,9,10,"A","J","K","Q"]

    #dealer hand/ player hand

    dealer=[]
    player=[]
    
    #deal cards

    def deal(turn): 
        card= random.choice(deck)
        turn.append(card)
        deck.remove(card)

    #get totals

    def total(hand):
        total = 0
        ace_11s = 0
        for card in hand:
            if card in range(11):
                total += card
            elif card in ['J', 'K', 'Q']:
                total += 10
            else:
                total += 11
                ace_11s += 1
        while ace_11s and total > 21:
            total -= 10
            ace_11s -= 1
        return total

    #check for winner

    def count_dealer_hand():
        if len(dealer) ==2:
            return dealer [0]
    

    #game loop

    for _ in range(2):
        deal(dealer)
        deal(player)

    #show hands
    
    while playerIn:
        print(f"\nDealer has {count_dealer_hand()} and ?")
        print(f"You have {player} for a total of {total(player)}")
        if playerIn:
            stayOrHit=input("1: Stay\n2: Hit\n")

        if stayOrHit=="1":
            playerIn=False
        else:
            deal(player)

        if total(player)>=21:
            break

    #winning and losing conditions

    if total(player)==21:
        print(f"\nYou have {player} for a total of {total(player)} and the Dealer has {dealer} for a total of {total(dealer)}")
        print ("Blackjack! Player Wins!")
        
    elif total(dealer)==21:
        print(f"\nYou have {player} for a total of {total(player)} and the Dealer has {dealer} for a total of {total(dealer)}")
        print ("Blackjack! Dealer Wins!")

    elif total(player)>21:
        print(f"\nYou have {player} for a total of {total(player)} and the Dealer has {dealer} for a total of {total(dealer)}")
        print("Player Bust, Dealer Wins!") 

    elif total(dealer)>21:
        print(f"\nYou have {player} for a total of {total(player)} and the Dealer has {dealer} for a total of {total(dealer)}")
        print("Dealer Bust, Player Wins!") 

    elif 21 - total(dealer) < 21 - total(player):
        print(f"\nYou have {player} for a total of {total(player)} and the Dealer has {dealer} for a total of {total(dealer)}")
        print("Dealer Wins!") 

    elif 21 - total(dealer) > 21 - total(player):
        print(f"\nYou have {player} for a total of {total(player)} and the Dealer has {dealer} for a total of {total(dealer)}")
        print("Player Wins!") 
        
