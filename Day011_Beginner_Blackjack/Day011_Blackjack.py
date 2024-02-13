import random
from art import logo

"""
############## Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def add_card():
    card = random.choice(cards)
    return card


def count_cards(user_cards, computer_cards):
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print("\n" * 100)  # simulate a clear effect
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    user_score = blackjack_check(user_cards)
    computer_score = blackjack_check(computer_cards)
    print(compare(user_score, computer_score))


def blackjack_check(bj_cards):
    if sum(bj_cards) == 21 and len(bj_cards) == 2:
        return 0
    else:
        return sum(bj_cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def ace_adding(new_card, cards_update):
    if new_card == 11 and (sum(cards_update) + new_card) > 21:
        cards_update.append(1)
    else:
        cards_update.append(new_card)
    return cards_update


play = True


def start_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_should_deal = True

    for i in range(2):
        user_cards.append(add_card())
        computer_cards.append(add_card())
    user_score = sum(user_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    while user_should_deal:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            user_should_deal = True
            new_card = add_card()
            user_cards = ace_adding(new_card, user_cards)
            user_score = sum(user_cards)

            if user_score > 21:
                user_should_deal = False
                count_cards(user_cards, computer_cards)
            else:
                print(f"   Your cards: {user_cards}, current score: {user_score}")
                print(f"   Computer's first card: {computer_cards[0]}")
        else:
            user_should_deal = False
            while sum(computer_cards) < 17:
                new_card = add_card()
                computer_cards = ace_adding(new_card, computer_cards)
            count_cards(user_cards, computer_cards)


while play:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        play = True
        start_game()
    else:
        print('Goodbye')
        play = False
