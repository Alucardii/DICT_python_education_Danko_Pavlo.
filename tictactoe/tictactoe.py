def print_board(board):
    print("---------", *("| " + " ".join(row) + " |" for row in board), "---------", sep="\n")
def read_input():
    while True:
        try:
            row, col = map(int, input("Enter the coordinates: ").split())
            if not (1 <= row <= 3) or not (1 <= col <= 3):
                print("Coordinates should be from 1 to 3!")
                continue
            return row, col
        except ValueError:
            print("You should enter numbers!")
def analyze_board(board):
    lines = board + list(map(list, zip(*board))) + [list(board[i][i] for i in range(3)), list(board[i][2 - i] for i in range(3))]

    x_wins = any(all(cell == "X" for cell in line) for line in lines)
    o_wins = any(all(cell == "O" for cell in line) for line in lines)
    x_count, o_count = sum(row.count("X") for row in board), sum(row.count("O") for row in board)

    if x_wins and o_wins or abs(x_count - o_count) >= 2:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif any("_" in row for row in board):
        return "Game not finished"
    else:
        return "Draw"
def make_move(board, player, row, col):
    if board[3 - row][col - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        board[3 - row][col - 1] = player
        return True

initial_board = [["_", "_", "_"]] * 3
current_board = [row[:] for row in initial_board]
print_board(current_board)

player = "X"
while True:
    row, col = read_input()
    if not make_move(current_board, player, row, col):
        continue
    print_board(current_board)
    result = analyze_board(current_board)
    print(result)
    if result in {"X wins", "O wins", "Draw"}:
        break
    player = "O" if player == "X" else "X"