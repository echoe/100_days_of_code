import art #You will need to comment this, and the art print statement, out to run this game on your machine.
import random
# Print the logo.
print(art.logo)

#Set the deck of cards.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def end_game(player_hand, dealer_hand, result):
    """When the game is over, tell you the result, and give you the chance to play again or not."""
    if input(f"Your hand was {player_hand} and the dealer's hand was {dealer_hand}. You {result}! Type y to play again") == "y":
        game()
    else:
        exit()

def game():
    """The main blackjack game logic. Deal, ask if you want to hit, and see how the game ends once that's done."""
    player_hand = []
    dealer_hand = []
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    dealer_hand.append(random.choice(cards))
    #Check for blackjack.
    if sum (player_hand) == 21:
        end_game(player_hand, dealer_hand, "win")
    elif sum(dealer_hand) == 21:
        end_game(player_hand, dealer_hand, "win")
    #Show the current state of the hand, and ask if you want to hit again. Check on if you bust after every hit.
    hit = "y"
    while hit == "y":
        hit = input(f"Your hand is {player_hand}, and the dealer's visible hand is {dealer_hand[0]}. "
                    f"Would you like to draw another card? Type y for yes, and n for no")
        if hit == "y":
            player_hand.append(random.choice(cards))
            if sum(player_hand) > 21:
                end_game(player_hand, dealer_hand, "lose")
    if sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
    if sum(player_hand) > sum(dealer_hand) or sum(dealer_hand) > 21:
        end_game(player_hand, dealer_hand, "win")
    else:
        end_game(player_hand, dealer_hand, "lose")

game()
