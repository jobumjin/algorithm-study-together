import sys

s = sys.stdin.readline().strip()

count = 0

i = 0
while True:
    if s[i] == 'c':
        if i < len(s) - 1:
            if s[i + 1] == '=' or s[i + 1] == '-':
                i = i + 1
                count += 1
            else:
                count += 1
        else:
            count += 1

    elif s[i] == 'd':
        if i < len(s) - 2:
            if s[i + 1] == '-':
                i = i + 1
                count += 1
            elif s[i + 1] == 'z':
                if s[i + 2] == '=':
                    i = i + 2
                    count += 1
                else:
                    count += 1
            else:
                count += 1

        elif len(s) - 2 <= i < len(s) - 1:
            if s[i + 1] == '-':
                i = i + 1
                count += 1
            else:
                count += 1

        else:
            count += 1

    elif s[i] == 'l':
        if i < len(s) - 1:
            if s[i + 1] == 'j':
                i = i + 1
                count += 1
            else:
                count += 1
        else:
            count += 1
    elif s[i] == 'n':
        if i < len(s) - 1:
            if s[i + 1] == 'j':
                i = i + 1
                count += 1
            else:
                count += 1
        else:
            count += 1
    elif s[i] == 's':
        if i < len(s) - 1:
            if s[i + 1] == '=':
                i = i + 1
                count += 1
            else:
                count += 1
        else:
            count += 1
    elif s[i] == 'z':
        if i < len(s) - 1:
            if s[i + 1] == '=':
                i = i + 1
                count += 1
            else:
                count += 1
        else:
            count += 1
    else:
        count += 1

    i += 1

    if i >= len(s):
        break

print(count)
