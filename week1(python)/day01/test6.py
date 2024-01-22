import sys

# count = 0
# def recursion(s, l, r):
#     global count
#     count += 1
#     if(l >= r): return 1
#     elif (s[l] != s[r]): return 0
#     else: return recursion(s, l+1, r-1)

# def isPalindrome(str):
#     return recursion(str, 0, len(str) - 1)

# N = int(sys.stdin.readline())
# for i in range(N):
#     count = 0
#     S = sys.stdin.readline().rstrip()
#     print(isPalindrome(S), count)

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merge(low_arr, high_arr)

def merge(l, h):
    result = []
    i = j = 0

    while i < len(l) and j <len(h):
        if l[i] < h[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(h[j])
            j += 1
    result.extend(l[i:])
    result.extend(h[j:])

    return result

A, K = map(int, sys.stdin.readline().split())
list_num = list(map(int, sys.stdin.readline().split()))

print(merge_sort(list_num))