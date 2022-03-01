import sys
from collections import deque

q = deque()

s = []
size = int(sys.stdin.readline())
for _ in range(size):
    # sys.stdin.readline()로 문자열을 입력받을 때엔 .strip()를 뒤에 추가해줘야 개행문자가 들어오지 않는다.
    do = sys.stdin.readline().strip()

    if "push_back" in do:
        # s.append(do.split()[1])
        q.append(do.split()[1])
    elif "push_front" in do:
        # s.append(do.split()[1])
        q.appendleft(do.split()[1])
    elif do == "pop_front":
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif do == "pop_back":
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif do == "size":
        print(len(q))
    elif do == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif do == "front":
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif do == "back":
        if len(q) > 0:
            print(q[len(q) - 1])
        else:
            print(-1)
