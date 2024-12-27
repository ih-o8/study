# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# lst = {}
# ans = []
#
# for i in range(n):
#     name = input().strip()
#     lst[name] = name
#
# for i in range(m):
#     try:
#         ans.append(lst[input().strip()])
#     except KeyError:
#         continue
#
# print(len(ans))
# ans.sort()
# for word in ans:
#     print(word)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
listener = [0] * n
watcher = [0] * m

for i in range(n):
    listener[i] = input().strip()

for j in range(m):
    watcher[j] = input().strip()

ans = list(set(listener) & set(watcher))
ans.sort()

print(len(ans))
ans.sort()
for word in ans:
    print(word)