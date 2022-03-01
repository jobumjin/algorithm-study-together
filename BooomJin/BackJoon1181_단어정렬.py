n = int(input())
word = []
for i in range(n):
    word.append(input())

set_word = set(word)
wordList = list(set_word)
wordList.sort()
wordList.sort(key = len)

for i in wordList:
    print(i)

## import sys  ## sys.stdin.readline()사용하면 입력시간 줄일 수 있음