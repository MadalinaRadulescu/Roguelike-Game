import random
import util
import engine
import ui

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3
itemes = {"apple": "*", "swoard": "!"}
boss = {"boss name": "Maduro Boss", "boss icon": "B", "HP": 100, "Power": 30}
BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def fight_boss(player, boss):
    print("Let the fight begin!")
    while True:
        user_choice = input("Do you want to fight? (y/n)")
        if user_choice == "n":
            print( player['player name'] + " you are a coward, " + boss['boss name'] + " has won the game!")
            break
        elif user_choice == "y":
            player["HP"] -= 22
            boss["HP"] -= 22
            if player["HP"] == 0:
                print(f"{boss['boss name']} has won the game! You lose hahahaha!")
                break
            if boss["HP"] == 0:
                print(f"Congratulation {player['player name']} you have won the game")
                break



def put_itemes_on_board(board, itemes, boss):
    board[random.randint(1, 18)][random.randint(1, 28)] = itemes["apple"]
    board[random.randint(1, 18)][random.randint(1, 28)] = itemes["swoard"]
    board[18][28] = boss["boss icon"]

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    name = input("Enter name: ")
    player = {"player name": name, "player_icon": "@", "HP": 50, "Power": 10,  "player position": [PLAYER_START_X, PLAYER_START_Y] }
    return player

def player_direction(key, board, row, col, player):
    if key == "W" or key == "w":
        if board[row-1][col] == "#":
            return row, col
        if board[row-1][col] == "!":
            player["Power"] += 30
        elif board[row-1][col] == "*":
            player["HP"] += 60
        elif board[row-1][col] == "B":
            fight_boss(player, boss)
        board[row][col] = " "
        return row - 1, col
    elif key == "S" or key == "s":
        if board[row+1][col] == "#":
            return row, col
        if board[row+1][col] == "!":
            player["Power"] += 30
        elif board[row+1][col] == "*":
            player["HP"] += 60
        elif board[row+1][col] == "B":
            fight_boss(player, boss)
        board[row][col] = " "
        return row+1, col
    elif key == "D" or key == "d":
        if board[row][col+1] == "#":
            return row, col
        if board[row][col+1] == "!":
            player["Power"] += 30
        elif board[row][col+1] == "*":
            player["HP"] += 60
        elif board[row][col+1] == "B":
            fight_boss(player, boss)
        board[row][col] = " "
        return row, col+1
    elif key == "A" or key == "a":
        if board[row][col-1] == "#":
            return row, col
        if board[row][col-1] == "!":
            player["Power"] += 30
        elif board[row][col-1] == "*":
            player["HP"] += 60
        elif board[row][col - 1] == "B":
            fight_boss(player, boss)
        board[row][col] = " "
        return row, col-1

def display_itemes(player, boss):

    for k, v in player.items():
        print(k + ": " + str(v))
    for k, v in boss.items():
        print(k + ": " + str(v))
     

def main():
    row, col = PLAYER_START_X, PLAYER_START_Y
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    put_itemes_on_board(board, itemes, boss)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player, row, col)
        ui.display_board(board, BOARD_WIDTH)
        display_itemes(player, boss)
        key = util.key_pressed()
        row, col = player_direction(key,board, row, col, player)
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
