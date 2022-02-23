import sys

count_01 = [0, 0, 0]


def count_up(target):
    if target == -1:
        count_01[0] += 1
    elif target == 0:
        count_01[1] += 1
    else:
        count_01[2] += 1


def display(boar):
    for bo in boar:
        print(bo)
    print('')


def sol(board, length):
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
        count_up(term)

    else:
        if length == 3:
            for i in range(3):
                for j in range(3):
                    count_up(board[i][j])
        else:
            for i in range(9):
                board_term = []

                div = int(i / 3)
                next_length = int(length / 3)
                nom = i % 3
                for j in range(next_length):
                    board_term.append(
                        board[j + (div * next_length)][(next_length * nom):next_length + (next_length * nom)])
                sol(board_term, next_length)


N = int(sys.stdin.readline())
first_board = []
for _ in range(N):
    first_board.append(list(map(int, sys.stdin.readline().split())))

sol(first_board, N)

print(count_01[0])
print(count_01[1])
print(count_01[2])