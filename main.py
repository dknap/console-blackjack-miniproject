import random
import art

print(art.logo)

def draw_a_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    return random.choice(cards)

def card_value(card):
    if card == "J" or card == "Q" or card == "K":               # convert J,Q,K,A cards to numeric value
        return 10
    elif card == "A":
        return 11
    else:
        return card

def play():
    player = []
    comp = []

    player.append(draw_a_card())                                        # draw a cards for player
    player.append(draw_a_card())

    player_score = card_value(player[0]) + card_value(player[1])        # total cards value
    print(f"Your cards: {player} | current score: {player_score}")

    comp.append(draw_a_card())                                          # draw a cards for computer
    comp.append(draw_a_card())

    comp_score = card_value(comp[0]) + card_value(comp[1])              # total cards value
    print(f"Computer's first card: {comp[0]} | value: {card_value(comp[0])}")

    while(player_score < 21):
        hit = input("Type 'y' to get another card or type 'n' to pass: ").lower()       # add another card
        if hit == "y":
            player.append(draw_a_card())
            player_score += card_value(player[-1])
            if player_score > 21:
                # TODO: check if ace in hand and convert to 1-value
                print(f"Your final hand: {player} | final score: {player_score}")   # player went over
                print(f"Computer's final hand: {comp} | final score: {comp_score}")
                print("You went over and you lose.")
                # TODO: go to play_again function

            elif player_score == 21:
                print(f"Your cards: {player} | final score: {player_score}")
                while (comp_score < 21):                                            # computer's hit
                    # TODO: Check computer
                    comp.append(draw_a_card())
                    comp_score += card_value(comp[-1])
                    if comp_score > 21:
                        # TODO: check if ace in comp's hand and convert to 1-value
                        print(f"Your final hand: {player} | final score: {player_score}")
                        print(f"Computer's final hand: {comp} | final score: {comp_score}")     # computer went over
                        print("Opponent went over, you win!")

                if comp_score == 21:
                    # TODO: print draw and go to play_again function
                    pass

            else:                                                               # player's score < 21 => ask for hit
                print(f"Your cards: {player} | current score: {player_score}")
        else:
            # TODO: Stand
            print(f"Your cards: {player} | current score: {player_score}")


play()