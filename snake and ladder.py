import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, dice_value):
    player += dice_value
    if player in snakes:
        print("Oops! Snake bite!")
        player = snakes[player]
    elif player in ladders:
        print("Yay! Ladder climb!")
        player = ladders[player]
    return player

def print_board(players):
    for position in range(1, 101):
        if position in players:
            print(players[position], end="\t")
        else:
            print(".", end="\t")
        if position % 10 == 0:
            print("\n")

def main():
    player1 = 1
    player2 = 1

    while True:
        input("Player 1, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"Player 1 rolled: {dice_value}")
        player1 = move_player(player1, dice_value)

        if player1 >= 100:
            print("Player 1 wins!")
            break

        print_board({player1: "P1", player2: "P2"})

        input("Player 2, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"Player 2 rolled: {dice_value}")
        player2 = move_player(player2, dice_value)

        if player2 >= 100:
            print("Player 2 wins!")
            break

        print_board({player1: "P1", player2: "P2"})

if __name__ == "__main__":
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    main()