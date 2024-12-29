# 메모리 초과
# from collections import deque
#
# n = int(input())
# step = [0] * (n + 1)
# for i in range(1, n+1):
#     step[i] = int(input())
#
# queue = deque([(0, 0, 0)])  # 연속, 인덱스, 총합
# ans = 0
#
# while queue:
#     cnt, idx, num = queue.popleft()
#     if cnt == 2 and idx + 2 <= n:
#         # 연속 2칸 올라오면 다음칸 못감. 다다음칸 가야함.
#         queue.append((1, idx + 2, num + step[idx + 2]))
#     elif cnt == 1:
#         # 다음 칸 가거나 다다음칸 갈 수 있음
#         if idx + 1 <= n:
#             queue.append((2, idx + 1, num + step[idx + 1]))
#         if idx + 2 <= n:
#             queue.append((1, idx + 2, num + step[idx + 2]))
#
#     elif cnt == 0:
#         # 다음 칸 가거나 다다음칸 갈 수 있음
#         if idx + 1 <= n:
#             queue.append((1, idx + 1, step[idx + 1]))
#         if idx + 2 <= n:
#             queue.append((1, idx + 2, step[idx + 2]))
#     if idx == n:
#         if num > ans:
#             ans = num
#
# print(ans)


# n = int(input())
# step = [0] * (n + 1)
# for i in range(1, 4):
#     step[i] = int(input())
# for j in range(4, n+1):
#     step[j] = max(step[j - 3] + step[j - 2], step[j - 3] + step[j - 1])
# print(step[n])

# f(4) = f(1) + f(2)
# f(4) = f(1) + f(3)

# def max_num(x):
#     ans = max(max_num(x - 3) + max_num(x - 2), max_num(x - 3) + max_num(x - 1))
#     return ans
#
# for i in range(4, n+1):
#     arr[i] = max_num(i)

n = int(input())
step = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    step[i] = int(input())
    if i == 1:
        dp[i] = step[i]
    elif i == 2:
        dp[i] = step[i-1] + step[i]
    else:
        dp[i] = max(dp[i - 3] + step[i - 1] + step[i], dp[i - 2] + step[i])

print(dp[-1])