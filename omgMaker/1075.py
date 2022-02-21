N = int(input())
P = int(input())

for i in range(0, 100):
    N_term = N - (N%100) + i
    if N_term % P == 0:
        if i < 10:
            result = '0' + str(i)
            print(result)
        else:
            print(i)

        break