import random
import AI
while True:
    player1choice = random.randint(1, 100)
    player2choice = random.randint(1, 100)
    if player1choice >= 50:
        if player2choice >= 50:
            player1years = 2
            player2years = 2
        if player2choice < 50:
            player1years = 0
            player2years = 3
    if player1choice < 50:
        if player2choice < 50:
            player1years = 1
            player2years = 1
        if player2choice >= 50:
            player2years = 0
            player1years = 3
    print(player1years)
    print(player2years)
    ans = input('play again ')
    if ans == 'no' or ans == 'n':
        break
