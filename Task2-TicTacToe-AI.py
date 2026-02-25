import math
board = [" " for _ in range(9)]
def print_board():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
def check_winner(player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False
def is_full():
    return " " not in board
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
def play_game():
    print("You are X, AI is O")
    print("Positions:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8")
    print()
    print_board()
    while True:
        move = int(input("Enter position (0-8): "))
        if board[move] != " ":
            print("Invalid move")
            continue
        board[move] = "X"
        print_board()
        if check_winner("X"):
            print("You Win!")
            break
        if is_full():
            print("Draw!")
            break
        ai_move()
        print_board()

        if check_winner("O"):
            print("AI Wins!")
            break
        if is_full():
            print("Draw!")
            break
play_game()
