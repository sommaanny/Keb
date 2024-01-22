import sys
count = 0
def recursion(s, l, r):
    global count
    count += 1
    if(l >= r): return 1
    elif (s[l] != s[r]): return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(str):
    return recursion(str, 0, len(str) - 1)

N = int(sys.stdin.readline())
for i in range(N):
    count = 0
    S = sys.stdin.readline().rstrip()
    print(isPalindrome(S), count)
