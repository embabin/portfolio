cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card_deck = {
    1: ["Ace of Hearts", [1,11]],
    2: ["Two of Hearts", 2],
    3: ["Three of Hearts", 3],
    4: ["Four of Hearts", 4],
    5: ["Five of Hearts", 5],
    6: ["Six of Hearts", 6],
    "Seven of Hearts": 7,
    "Eight of Hearts": 8,
    "Nine of Hearts": 9,
    "Ten of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "Ace of Diamonds": [1,11],
    "Two of Diamonds": 2,
    "Three of Diamonds": 3,
    "Four of Diamonds": 4,
    "Five of Diamonds": 5,
    "Six of Diamonds": 6,
    "Seven of Diamonds": 7,
    "Eight of Diamonds": 8,
    "Nine of Diamonds": 9,
    "Ten of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
    "Ace of Clubs": [1,11],
    "Two of Clubs": 2,
    "Three of Clubs": 3,
    "Four of Clubs": 4,
    "Five of Clubs": 5,
    "Six of Clubs": 6,
    "Seven of Clubs": 7,
    "Eight of Clubs": 8,
    "Nine of Clubs": 9,
    "Ten of Clubs": 10,
    "Jack of Clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10,
    "Ace of Spades": [1,11],
    "Two of Spades": 2,
    "Three of Spades": 3,
    "Four of Spades": 4,
    "Five of Spades": 5,
    "Six of Spades": 6,
    "Seven of Spades": 7,
    "Eight of Spades": 8,
    "Nine of Spades": 9,
    "Ten of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
}

import art
from art import blackjackart
import random
dealer_score = -1
bet = 0
bankroll = 100

def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card
    
def calculate_score(cards):
    """Takes list of cards and returns score when calculating the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player,dealer):
    if player == dealer:
        return "You Draw"
    elif dealer == 0:
        return "You Lose, dealer has Blackjack"
    elif player == 0:
        return "You Win, you have Blackjack"
    elif player > 21:
        return "You Lose"
    elif dealer > 21:
        return "You Win"
    elif player <= 21 and player > dealer:
        return "You Win"
    elif dealer > player:
        return "You Lose"
    else:
        return "Invalid Game Entry"

def playgame():
    dealer_hand = []
    player_hand = []
    game_won = False
    isgameover = False

    #Deal the cards
    for _ in range(2):
        new_card = deal_card()
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    #Determine hands on each side
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your cards are {player_hand} totaling to {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    while not isgameover:
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            isgameover = True
        else:
            player_deal = input("Do you want to take another card? 'y' if so")
            if player_deal == "y":
                player_hand.append(deal_card())
                player_score = calculate_score(player_hand)
                print(f"Your cards are {player_hand} totaling to {player_score}")
            else:
                isgameover = True
    print(player_hand)
    print(dealer_hand)
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    print(dealer_hand)

    return compare(player_score,dealer_score)

def changemoney(bank, wager, result):
    if result == "You Win":
        bank += wager
    elif result == "You Win, you have Blackjack":
        bank += (wager * 1.5)
    elif result == "You Draw":
        pass
    else:
        bank -= wager
    return bank

while bankroll > 0:
    #Display your current chips
    print(blackjackart)
    print(f"Your current bankroll is {bankroll}")
    #Set a new bet
    bet = int(input("How much would you like to bet?\n"))
    endhand = playgame()
    print(endhand)
    bankroll = changemoney(bankroll, bet, endhand)
    player_hand = []
    dealer_hand = []
    isgameover = False