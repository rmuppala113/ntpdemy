board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} |{} |".format(board[0],board[1],board[2])
    row2 = "| {} | {} |{} |".format(board[3],board[4],board[5])
    row3 = "| {} | {} |{} |".format(board[6],board[7],board[8])
    print
    print(row1)
    print(row2)
    print(row3)
    print
def move(player):
    if player == "X":
        number = 1
    else:
        number = 2
    print("Player {}, your turn".format(number))
    choice = int(raw_input("Enter your number(1-9): ").strip())
    if board[choice - 1] == "  ":
        board[choice - 1] = player
    else:
        print("That place is taken")

def victory(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return  True
    else:
        return False
def draw():
    if "  " not in board:
        return  True
    else:
        return  False

while True:
    print_board()
    move("X")
    print_board()
    if victory("X"):
        print("X Wins...!")
        break
    move("O")
    print_board()
    if victory("O"):
        print("O wins...!")
        break
    elif draw():
        print("Its Draw...!")
        break




