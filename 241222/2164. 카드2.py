from collections import deque

arr = deque([n for n in range(1, int(input()) + 1)])

num = len(arr)

while num > 1:
    arr.popleft()
    num -= 1
    card = arr.popleft()
    arr.append(card)

print(arr[0])