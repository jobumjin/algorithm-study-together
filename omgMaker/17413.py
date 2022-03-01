All = input()

status = True
term = []
result = ''

for i in range(len(All)):
    if not status:
        if All[i] == '>':
            status = True
        result += All[i]

    else:
        if All[i] == ' ':
            if len(term) == 0:
                continue
            elif len(term) == 1:
                result += term[0]
                term = []
            else:
                for j in range(len(term) - 1, -1, -1):
                    result += term[j]
                term = []

            result += All[i]

        elif All[i] == '<':
            if len(term) == 1 or len(term) == 0:
                if len(term) == 1:
                    result += term[0]
                    term = []
            else:
                for j in range(len(term) - 1, -1, -1):
                    result += term[j]
                term = []

            result += All[i]
            status = False
        else:
            term.append(All[i])

if len(term) > 0:
    for j in range(len(term) - 1, -1, -1):
        result += term[j]

print(result)