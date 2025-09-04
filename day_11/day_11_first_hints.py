import art
import random
"""
This is the version of the game that sticks to the flowchart that was shared in the program but is still fully written by me. 
"""

# Print the logo.
print(art.logo)

#Set the requirements.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_again():
    """When the game is over, tell you the result, and give you the chance to play again or not."""
    if input(f"Type y to play again") == "y":
        game()
    else:
        exit()

def check_score(player_hand, dealer_hand):
    if sum(player_hand) == 21 and 10 in player_hand and 11 in player_hand:
        print("Blackjack! You win!")
        play_again()
    if sum(dealer_hand) == 21 and 10 in dealer_hand and 11 in dealer_hand:
        print("Dealer gets Blackjack! You lose!")
        play_again()
    if sum(player_hand) > 21:
        if 11 in player_hand:
            if sum(player_hand) > 31:
                print(f"You went bust! Your hand was {player_hand}.")
                play_again()
            else:
                pass# continue
        else:
            print(f"You went bust! Your hand was {player_hand}.")
            play_again()
    if sum(dealer_hand) > 21:
        if 11 in dealer_hand:
            if sum(dealer_hand) > 31:
                print(f"The dealer went bust! Their hand was {dealer_hand}.")
                play_again()
            else:
                pass# continue
        else:
            print("The dealer went bust! Their hand was {dealer_hand}.")
            play_again()

def game():
    """The main blackjack game logic. Deal, ask if you want to hit, and see how the game ends once that's done."""
    player_hand = []
    dealer_hand = []
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    #Check for blackjack.
    check_score(player_hand, dealer_hand)
    #Show the current state of the hand, and ask if you want to hit again. Check on if you bust after every hit.
    hit = "y"
    while hit == "y":
        hit = input(f"Your hand is {player_hand}, and the dealer's visible hand is {dealer_hand[0]}. "
                    f"Would you like to draw another card? Type y for yes, and n for no")
        if hit == "y":
            player_hand.append(random.choice(cards))
            check_score(player_hand, dealer_hand)
    # Dealer hits until they're 17 or higher total, then stops
    if sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
    check_score(player_hand, dealer_hand)
    #If nobody bust, we compare hands to see who won. Dealer wins ties
    if sum(player_hand) > sum(dealer_hand):
        print(f"You win! Your hand was {player_hand}. The dealer had {dealer_hand}.")
    else:
        print(f"You lose! Your hand was {player_hand}. The dealer had {dealer_hand}.")
    play_again()

game()