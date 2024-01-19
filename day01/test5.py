import sys

N, M = map(int, sys.stdin.readline().split())
word_book = dict()

for i in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word in word_book:
            word_book[word] += 1
        else:
            word_book[word] = 1

result_book = sorted(word_book.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for keys, values in result_book:
    print(keys)