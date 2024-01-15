sum = 1 + \
2 + \
3 + \
4
print(sum)
print()

import sys
letter = sys.stdin.readline().rstrip()
vowel = {'a', 'e', 'i', 'o', 'u'}
if letter in vowel:
    print(f'{letter} is vowel')
else:
    print(f'{letter} is not vowel')