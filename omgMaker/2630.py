import sys

count_01 = [0, 0]


def display(boar):
    for bo in boar:
        print(bo)

    print('')


def sol(board, length):
    # 현재 크기가 1 * 1 인지 확인한다.
    # 맞다면 0,0 칸에 해당하는 값이 무엇인지 확인하고 카운트를 +1 한다.
    if length == 1:
        count_01[board[0][0]] += 1

    # 현재 크기가 1 * 1 이 아니라면,
    # 현재 상자가 한 색깔의 색종이인지 검사한다.
    # 첫 좌표의 값이 0 인지 1 인지 저장하고 (term),
    # 다음 값 중에서 다른 값이 한번이라도 나오면(if [][] != term) break,
    # 끝까지 같은 값이었으면 term 의 카운트를 + 1
    else:
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
            count_01[term] += 1

        # 한 색깔의 색종이가 아니라면, 현재 색종이를 4개로 나눈다.
        # for i in range(4)문으로 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래를 나눈다.
        # 나눠진 board와 한 변의 길이를 매개변수로 줘서 sol()을 실행한다.
        else:
            for i in range(4):
                board_term = []
                for j in range(int(length / 2)):
                    board_term.append(
                        board[j + ((int(i / 2)) * (int(length / 2)))]
                        [(int(length / 2) * (i % 2)):int(length / 2) + (int(length / 2) * (i % 2))]
                    )
                sol(board_term, int(length / 2))


N = int(sys.stdin.readline())
first_board = []
for _ in range(N):
    first_board.append(list(map(int, sys.stdin.readline().split())))

sol(first_board, N)

print(count_01[0])
print(count_01[1])

