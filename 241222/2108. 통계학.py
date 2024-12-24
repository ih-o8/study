import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
print(round(sum(arr) / n))

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(arr[n // 2])

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
mode = Counter(arr)
mode = mode.most_common()
if len(mode) == 1:
    print(mode[0][0])
else:
    if mode[0][1] > mode[1][1]:
        print(mode[0][0])
    else:
        print(mode[1][0])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(arr[-1] - arr[0])