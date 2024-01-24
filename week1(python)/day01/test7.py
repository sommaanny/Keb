# def kantor(s, N):   #백준 4779
#     if N == 1:
#         return
#     for i in range(s + N//3, s + (N // 3) * 2):
#         list_line[i] = ' '
#     kantor(s, N // 3)
#     kantor(s + (N // 3) * 2, N // 3)


# while True:
#     try:
#         N = int(input())
#         list_line = ['-' for i in range(3 ** N)]
#         kantor(0,3 ** N)
#         print(''.join(list_line))
#     except EOFError:
#         break

def N_stars(N):
    if N == 3:
        return ['***', '* *', '***']
    arr = N_stars(N // 3)
    stars = []

    for i in arr:
        stars.append(i * 3)
    for i in arr:
        stars.append(i + ' ' * (N // 3) + i)
    for i in arr:
        stars.append(i * 3)
    return stars

N = int(input())
print('\n'.join(N_stars(N)))