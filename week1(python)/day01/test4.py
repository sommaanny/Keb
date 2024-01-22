import sys

# # N = int(sys.stdin.readline())  #백준 26069
# # count = 1
# # dic_p = {}

# # for i in range(N):
# #     people1, people2 = sys.stdin.readline().rstrip().split()
# #     if people1 == "ChongChong" or people2 == "ChongChong":
# #         if people1 != "ChongChong":
# #             dic_p[people1] = 1
# #         else:
# #             dic_p[people2] = 1
# #     elif people1 in dic_p:
# #         dic_p[people2] = 1
# #     elif people2 in dic_p:
# #         dic_p[people1] = 1

# # for _ in dic_p:
# #     count += 1

# # print(count)
# ----------------------------------

# N = int(sys.stdin.readline())   #백준 2108
# list_num = []

# for i in range(N):
#     list_num.append(int(sys.stdin.readline()))

# # 산술평균
# if (sum(list_num) / N - sum(list_num) // N) >= 0.5:
#     print(sum(list_num) // N + 1)
# else:
#     print(sum(list_num) // N)

# # 중앙값
# sorted_list_num = sorted(list_num)
# print(sorted_list_num[N // 2])

# #최빈값
# dic_num = {}
# for _ in list_num:
#     if _ in dic_num:
#         dic_num[_] += 1
#     else:
#         dic_num[_] = 1

# max_num = max(dic_num.values())
# result_list = []
# for keys, values in dic_num.items():
#     if values == max_num:
#         result_list.append(keys)
# result_list.sort()

# if len(result_list) >= 2:
#     print(result_list[1])
# else:
#     print(result_list[0])

# #범위
# print(max(list_num) - min(list_num))
# ------------------------------------------------
