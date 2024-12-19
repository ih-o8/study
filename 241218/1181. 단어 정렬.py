# 길이가 짧은 것부터, 사전 순, 중복 제거

# 시간 초과
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = [[0] * n for _ in range(51)]
# cnt = [0] * 51
# for i in range(n):
#     string = input().strip()
#     # strip()으로 개행문자를 제거하지 않으면 글자 개수 +1
#     num = len(string)
#     if string not in arr[num]:
#         for j in range(n):
#             if arr[num][j] == 0:
#                 arr[num][j] = string
#                 cnt[num] += 1
#                 break
#
# for k in range(1, 51):
#     if cnt[k] == 1:
#         print(arr[k][0])
#     elif cnt[k] > 1:
#         for x in range(n - cnt[k]):
#             arr[k].pop()
#         arr[k].sort()
#         for y in arr[k]:
#             print(y)

import sys
input = sys.stdin.readline

arr = []

for _ in range(int(input())):
    arr.append(input().strip())

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for word in arr:
    print(word)
