from main import PLAYER_START_X, PLAYER_START_Y


def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    items = ["🎆", "🍉"]
    index_of_items = 0

    
    wall = []
    board = []
    for _ in range(width):
        wall.append(items[index_of_items + 1])
    board.append(wall.copy())
    for column in range(height-2):
        row = []
        for index in range(width):
            if index == 0 or index == width-1: #elif
                row.append(items[index_of_items + 1])
            else:
                row.append(items[index_of_items + 0])
        board.append(row.copy())
    board.append(wall.copy())
    return board
    # board =[]
    # for i in range(height):
    #     i = []
    #     board.append(i)
    #     for j in range(width):
    #         j = "."
    #         i.append(j)

    # return board
    


def put_player_on_board(board, player, row, col):
    for i in board:
        if player["player_icon"] not in i:
            board[row][col] = player["player_icon"]
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''

