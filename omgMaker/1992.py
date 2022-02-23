import sys

result_str = ''


def display(boar):
    for bo in boar:
        print(bo)
    print('')


def sol(board, length):
    global result_str

    term = board[0][0]

    true_all_same = True
    for i in range(length):
        true_i_same = True

        for j in range(length):
            if i == 0 and j == 0:
                continue
            else:
                if board[i][j] != term:
                    true_i_same = False
                    break

        if not true_i_same:
            true_all_same = False
            break
    if true_all_same:
        result_str += str(term)

    else:
        result_str += '('

        cal_val = 2
        if length == cal_val:
            for i in range(cal_val):
                for j in range(cal_val):
                    result_str += str(board[i][j])
        else:

            for i in range(cal_val ** 2):
                board_term = []

                div = int(i / cal_val)
                next_length = int(length / cal_val)
                nom = i % cal_val

                for j in range(next_length):
                    board_term.append(board[j + (div * next_length)][(next_length * nom):next_length + (next_length * nom)])
                sol(board_term, next_length)

        result_str += ')'


N = int(sys.stdin.readline())
first_board = []
first_board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

sol(first_board, N)

# display(first_board)
print(result_str)
