def make_board(value=" "):
    table = []
    for _ in range(3):
        inner_list = []
        table.append(inner_list)
        for _ in range(3):
            inner_list.append(value)
    return table

def print_board(board):
    for row in board:
        for column in row:
            print(column, end='')
        print()
    return

def make_move(board, current_symbol):
    try:
        user_input_row,user_input_col = int(input("Enter row:")),int(input("Enter column:"))
        if board[user_input_row][user_input_col] == "X" or board[user_input_row][user_input_col] == "O":
            raise ValueError("Invalid Location Please Try Again")
        else:
            board[user_input_row][user_input_col] = current_symbol
            print_board(board)
    except ValueError:
        make_move(board,current_symbol)


def main():
    table = make_board()
    # print_board(table)
    make_move(table, "X")
    make_move(table, "O")

if __name__ == "__main__":
    main()