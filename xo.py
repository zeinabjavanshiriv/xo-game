import random


def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]}  | {board[i + 1]}  | {board[i + 2]}")
        if i < 6:
            print("----+----+----")
    print("\n")


def winner_check(board, player):
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    return any(all(board[i] == player for i in w) for w in wins)


def is_full(board):
    return all(c != " " for c in board)


def find_best_move(board, player):
    opponent = "O" if player == "X" else "X"
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            if winner_check(board, player):
                board[i] = " "
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if winner_check(board, opponent):
                board[i] = " "
                return i
            board[i] = " "

    if board[4] == " ":
        return 4

    corners = [0, 2, 6, 8]
    available = [c for c in corners if board[c] == " "]
    if available:
        return random.choice(available)

    empty = [i for i in range(9) if board[i] == " "]

    return random.choice(empty)


name = input("Enter your name: ").capitalize()


def play_game():
    board = [" "] * 9
    choose = input("Choose between X and O: ").upper()
    if choose == "X":
        computer = "O"
        human = "X"
    elif choose == "O":
        computer = "X"
        human = "O"
    else:
        print("Choose between X and O")

    starter = input(
        f"==================\nHey! Welcome to our XO game\n{name} is  playing\n{name} is: {human} computer is: {computer}\nWhich one should start?\n1.You\n2.Computer\n==================\n"
    )
    current = computer if starter == "2" else human
    while True:
        print_board(board)
        if current == human:
            try:
                move = int(input("Choose place around 0-8: "))
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid input")
                    continue
            except ValueError:
                print("Input number!")
                continue
        else:
            print("Computer is thinking!")
            move = find_best_move(board, current)
            print(f"Computer chooses: {move}")

        board[move] = current

        if winner_check(board, current):
            print_board(board)
            if current == human:
                print(f"{name} won")
            else:
                print("Computer won!")
            break

        if is_full(board):
            print_board(board)
            print("it's draws!")
            break

        current = computer if current == human else human

    again = input("Play again?\n1.Yes\n2.No\n")
    if again == "1":
        play_game()


if __name__ == "__main__":
    play_game()
