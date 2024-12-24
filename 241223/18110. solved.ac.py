import sys
input = sys.stdin.readline

from collections import deque

def check_num(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())

    arr.sort()
    num_list = deque(arr)

    p = check_num(n * 0.15)

    for i in range(p):
        num_list.popleft()
        num_list.pop()
        n -= 2

    print(check_num(sum(num_list) / n))