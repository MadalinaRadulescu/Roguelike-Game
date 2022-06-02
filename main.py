import random
import util
import engine
import ui

PLAYER_START_X = 3
PLAYER_START_Y = 3
itemes = {"bread": "🍞", "swoard": "🔪", "armor": "🧪"}
boss = {"boss name": "Maduro Boss", "boss icon": "👺", "HP": 100, "Power": 30}
BOARD_WIDTH = 30
BOARD_HEIGHT = 20

def fight_boss(player, boss):
    print("\nLet the fight begin!")
    while True:
        user_choice = input("\nDo you want to fight? (y/n)\n")
        if user_choice == "n":
            return 1
        elif user_choice == "y":
            if player["armor"] > 0:
                player["HP"] -= 10
                player["armor"] -= 10
                boss["HP"] -= 22
                boss["Power"] -= 6
                display_itemes(player, boss)
            else:
                player["HP"] -= 22
                player["Power"] -= 8
                boss["HP"] -= 22
                boss["Power"] -= 6
                display_itemes(player, boss)
            if player["HP"] < 0 or player["Power"]<0:
                return 2
            if boss["HP"] < 0 or boss["Power"]<0:
                return 3



def put_itemes_on_board(board, itemes, boss):
    board[random.randint(1, 18)][random.randint(1, 28)] = itemes["bread"]
    board[random.randint(1, 18)][random.randint(1, 28)] = itemes["swoard"]
    board[random.randint(1, 18)][random.randint(1, 28)] = itemes["armor"]
    board[3][25] = boss["boss icon"]

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    name = input("Enter name: ")
    player = {"player name": name, "player_icon": "😃", "HP": 50, "Power": 10, "armor": 0,  "player position": [PLAYER_START_X, PLAYER_START_Y] }
    return player

def player_direction(key, board, row, col, player):
    if key == "W" or key == "w":
        if board[row-1][col] == "🍉":
            return row, col
        elif board[row-1][col] == boss["boss icon"]:
            return row, col
        elif board[row-1][col] == itemes["swoard"]:
            player["Power"] += 30
        elif board[row-1][col] == itemes["bread"]:
            player["HP"] += 60
        elif board[row-1][col] == itemes["armor"]:
            player["armor"] += 30
        board[row][col] = "🎆"
        return row - 1, col
    elif key == "S" or key == "s":
        if board[row+1][col] == "🍉":
            return row, col
        elif board[row+1][col] == boss["boss icon"]:
            return row, col
        elif board[row+1][col] == itemes["swoard"]:
            player["Power"] += 30
        elif board[row+1][col] == itemes["bread"]:
            player["HP"] += 60
        elif board[row+1][col] == "⛓":
            player["armor"] += 30
        board[row][col] = "🎆"
        return row+1, col
    elif key == "D" or key == "d":
        if board[row][col+1] == "🍉":
            return row, col
        elif board[row][col+1] == boss["boss icon"]:
            return row, col
        elif board[row][col+1] == itemes["swoard"]:
            player["Power"] += 30
        elif board[row][col+1] == itemes["bread"]:
            player["HP"] += 60
        elif board[row][col+1] == itemes["armor"]:
            player["armor"] += 30
        board[row][col] = "🎆"
        return row, col+1
    elif key == "A" or key == "a":
        if board[row][col-1] == "🍉":
            return row, col
        elif board[row][col-1] == boss["boss icon"]:
            return row, col
        elif board[row][col-1] == itemes["swoard"]:
            player["Power"] += 30
        elif board[row][col-1] == itemes["bread"]:
            player["HP"] += 60
        elif board[row][col-1] == itemes["armor"]:
            player["armor"] += 30
        board[row][col] = "🎆"
        return row, col-1

def display_itemes(player, boss):

    for k, v in player.items():
        print(k + ": " + str(v))
    print()
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
        winner = 0
        engine.put_player_on_board(board, player, row, col)
        ui.display_board(board, BOARD_WIDTH)
        display_itemes(player, boss)
        if board[row-1][col] == "👺":
            winner = fight_boss(player, boss)
        elif board[row+1][col] == "👺":
            winner = fight_boss(player, boss)
        elif board[row][col-1] == "👺":
            winner = fight_boss(player, boss)
        elif board[row][col+1] == "👺":
            winner = fight_boss(player, boss)
        if winner == 1:
            print( "\n"+ player['player name'] + " you are a coward, " + boss['boss name'] + " has won the game!\n")
            break
        elif winner == 2:
            print(f"\n{boss['boss name']} has won the game! You lose hahahaha!\n")
            break
        elif winner == 3:
            print(f"\nCongratulation {player['player name']} you have won the game\n")
            break
        key = util.key_pressed()
        row, col = player_direction(key, board, row, col, player)
        if key == 'q':
            is_running = False
        else:
            pass
        util.clear_screen()


if __name__ == '__main__':
    main()
