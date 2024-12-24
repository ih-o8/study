from collections import Counter

n = int(input())
num_lst = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

num_lst = Counter(num_lst)
ans = [0] * m

for i in range(m):
    ans[i] = num_lst[arr[i]]

print(*ans)