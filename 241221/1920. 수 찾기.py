# 딕셔너리 활용
import sys
input = sys.stdin.readline

n = int(input())
dict = set(map(int, input().split()))
m = int(input())
number = list(map(int, input().split()))

for i in number:
    if i in dict:
        print(1)
    else:
        print(0)


# 이진 탐색
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
num_lst = list(map(int, input().split()))

arr.sort()
for num in num_lst:
    low = 0
    high = n - 1
    if num == arr[low] or num == arr[high]:
        print(1)
    elif arr[low] < num < arr[high]:
        while low < high:
            mid = (low + high) // 2
            if num == arr[mid]:
                print(1)
                break
            elif num < arr[mid]:
                high = mid
            elif num > arr[mid]:
                low = mid
            if high - low == 1:
                print(0)
                break
    else:
        print(0)