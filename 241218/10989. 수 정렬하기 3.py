# 메모리 초과
# arr = []
# for _ in range(int(input())):
#     arr.append(int(input()))
# arr.sort()
# for i in arr:
#     print(i)

# 메모리 초과
# import sys
# arr = []
# for _ in range(int(input())):
#     arr.append(sys.stdin.readline())
# arr.sort()
# for i in arr:
#     print(i)

import sys
input = sys.stdin.readline

arr = [0] * 10001
# 10,000보다 작거나 같은 자연수
for _ in range(int(input())):
    arr[int(input())] += 1
for i in range(1, 10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)