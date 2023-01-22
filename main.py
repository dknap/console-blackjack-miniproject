import random
import art

print(art.logo)


def draw_a_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    return random.choice(cards)

player1 = draw_a_card()
player2 = draw_a_card()

if player1 == "J" or player1 == "Q" or player1 == "K":
    player_card1 = 10
elif player1 == "A":
    player_card1 = 11
else:
    player_card1 = player1
if player2 == "J" or player2 == "Q" or player2 == "K":
    player_card2 = 10
elif player2 == "A":
    player_card2 = 11
else:
    player_card2 = player2

player_score = player_card1 + player_card2
print(f"Your cards: [{player1}], [{player2}] | current score: {player_score}")
