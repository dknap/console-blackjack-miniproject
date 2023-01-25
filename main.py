import random
import art

print(art.logo)
# TODO: improve UX: show the drawn card


def draw_a_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    return random.choice(cards)


def card_value(card):
    if card == "J" or card == "Q" or card == "K":  # convert J,Q,K,A cards to numeric value
        return 10
    elif card == "A":
        return 11
    else:
        return card


def play_again():
    again = input("Type 'y' to play again or anything to exit: ").lower()  # ask user to play again
    if again == "y":
        play()  # clear variables and start new game
    else:
        end_game()  # print final message


def end_game():
    print("Thank you for the time we spent together. See you soon! \nExiting...")
    exit()


def ace_value(ace, hand):
    if hand <= 21:
        return ace
    else:
        ace = 1
        return ace


def play():
    player = []
    comp = []

    player.append(draw_a_card())  # draw a cards for player
    player.append(draw_a_card())

    player_score = card_value(player[0]) + card_value(player[1])  # total cards value
    print(f"Your cards: {player} | current score: {player_score}")

    comp.append(draw_a_card())  # draw a cards for computer
    comp.append(draw_a_card())

    comp_score = card_value(comp[0]) + card_value(comp[1])  # total cards value
    print(f"Computer's first card: [{comp[0]}] | value: {card_value(comp[0])}")

    if player_score == 21:  # player's BJ
        print("=== BLACKJACK! ===")
        print(f"Computer's hand: {comp} | final score: {comp_score}")
        if comp_score == player_score:  # comp's BJ = draw
            print("But unfortunately dealer has the same... Draw!")
        else:
            print("You win!")
            art.line()
            play_again()
    else:
        while player_score < 21:

            hit = input("Type 'y' to get another card or type 'n' to pass: ").lower()  # add another card
            if hit == "y":
                player.append(draw_a_card())
                print(player[-1])  # testing (to del)
                player_score += card_value(player[-1])
                if player_score < 21:
                    print(f"Your cards: {player} | current score: {player_score}")
                else:
                    for card in range(len(player)):
                        if player[card] == "A":
                            player[card] = 1
                            player_score -= 10
                            print(f"Your cards: {player} | current score: {player_score}")
                    if player_score > 21:
                        art.line()
                        print(f"Your final hand: {player} | final score: {player_score}")  # player went over
                        print(f"Computer's final hand: {comp} | final score: {comp_score}")
                        print("You went over and you lose.")
                        art.line()
                        play_again()
                    else:
                        # print(f"Your cards: {player} | current score: {player_score}")
                        pass
                if player_score == 21:
                    # print(f"Your cards: {player} | final score: {player_score}")
                    while comp_score < 17:  # computer's hit
                        comp.append(draw_a_card())
                        comp_score += card_value(comp[-1])
                        if 16 < comp_score < 21:
                            art.line()
                            print(f"Your final hand: {player} | final score: {player_score}")
                            print(f"Computer's final hand: {comp} | final score: {comp_score}")  # computer went over
                            print("You win!")
                            art.line()
                            play_again()
                        elif comp_score > 21:
                            have_ace = False
                            for card in range(len(comp)):
                                if comp[card] == "A":
                                    have_ace = True
                                    comp[card] = 1
                                    comp_score -= 10
                                    print(f"Your cards: {player} | current score: {player_score}")
                            if have_ace == False:
                                art.line()
                                print(f"Your final hand: {player} | final score: {player_score}")
                                print(
                                    f"Computer's final hand: {comp} | final score: {comp_score}")  # computer went over
                                print("Opponent went over, you win!")
                                art.line()
                                play_again()
                    if comp_score == 21:
                        player_cards = len(player)
                        comp_cards = len(comp)
                        if player_cards < comp_cards:
                            print("You win!")
                        elif player_cards == comp_cards:
                            print("Draw.")
                        else:
                            print("You lose.")
                        art.line()
                        play_again()
                    if 16 < comp_score < 21:
                        art.line()
                        print(f"Your final hand: {player} | final score: {player_score}")
                        print(f"Computer's final hand: {comp} | final score: {comp_score}")  # computer went over
                        print("You win!")
                        art.line()
                        play_again()
                else:  # player's score < 21
                    pass
            else:  # IF HIT == NO
                if comp_score > player_score:
                    art.line()
                    print(f"Your final hand: {player} | final score: {player_score}")
                    print(f"Computer's final hand: {comp} | final score: {comp_score}")  # computer > player
                    print("You lose.")
                    art.line()
                    play_again()
                elif comp_score > 16 and comp_score == player_score:
                    print("Draw.")
                while comp_score < player_score:  # computer's hit
                    if comp_score <= 16:
                        comp.append(draw_a_card())
                        comp_score += card_value(comp[-1])
                        if comp_score > 21:
                            have_ace = False
                            for card in range(len(comp)):
                                if comp[card] == "A":
                                    have_ace = True
                                    comp[card] = 1
                                    comp_score -= 10
                    else:
                        art.line()
                        print(f"Your final hand: {player} | final score: {player_score}")
                        print(f"Computer's final hand: {comp} | final score: {comp_score}")
                        print("You win!")
                        art.line()
                        break

                if 16 < comp_score <= 21:
                    art.line()
                    print(f"Your final hand: {player} | final score: {player_score}")
                    print(f"Computer's final hand: {comp} | final score: {comp_score}")
                    if player_score > comp_score:  # check who win
                        print("You win!")
                        play_again()
                    elif player_score < comp_score:
                        print("You lose!")
                        play_again()
                    else:
                        player_cards = len(player)  # cards counting
                        comp_cards = len(comp)
                        if player_cards < comp_cards:
                            print("You win!")
                        elif player_cards == comp_cards:
                            print("Draw.")
                        else:
                            print("You lose.")
                    art.line()
                    play_again()
                elif comp_score > 21:
                    have_ace = False
                    for card in range(len(comp)):
                        if comp[card] == "A":
                            have_ace = True
                            comp[card] = 1
                            comp_score -= 10
                    if not have_ace:
                        art.line()
                        print(f"Your final hand: {player} | final score: {player_score}")
                        print(f"Computer's final hand: {comp} | final score: {comp_score}")  # computer went over
                        print("Opponent went over, you win!")
                        art.line()
                        play_again()
                # print(f"Your cards: {player} | current score: {player_score}")


play()
