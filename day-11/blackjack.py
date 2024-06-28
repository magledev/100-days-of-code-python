########################################### Blackjack Project ##############################################

################# House Rules ###################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King are equal to 10.
# The Ace can count as either 1 or 11.
# The cards in the list have equal probability of being drawn.
# Cards are not removed fro the deck as they are drawn.

import random
import clear_screen
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_scores(player_score, dealer_score):
    if player_score == dealer_score:
        return "It's a draw"
    elif dealer_score == 0:
        return"Dealer has Blackjack"
    elif player_score == 0:
        return"Player has Blackjack"
    elif player_score > 21:
        return"Player busts"
    elif dealer_score > 21:
        return"Dealer busts"
    elif player_score > dealer_score:
        return"Player wins"
    else:
        return"Dealer wins"


def play_game():
    print(art.logo)
    player_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\nPlayer cards: {player_cards}, current total: {player_score}")
        print(f"\nDealer revealed card: {dealer_cards[1]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            draw_again = input(
                "\nType 'y' for another card or Type 'n' to pass: ").lower()
            if draw_again == "y":
                player_cards.append(deal_card())
                print(calculate_score(player_cards))
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(
        f"\nPlayer's hand: {player_cards} which scores: {player_score}\n\nDealer's scores: {dealer_cards} which scores: {dealer_score}")
    print(f"\n{compare_scores(player_score, dealer_score)}")


while input("\nDo you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ") == 'y':
    clear_screen.clear()
    play_game()
