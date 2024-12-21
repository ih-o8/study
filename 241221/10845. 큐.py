from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])
for _ in range(int(input())):
    arr = input().split()
    if arr[0] == 'push':
        # 정수를 큐에 넣는 연산
        queue.append(arr[-1])
    elif arr[0] == 'pop':
        # 가장 앞에 있는 정수를 빼고 수를 출력. 정수가 없는 경우 -1을 출력
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif arr[0] == 'size':
        # 정수의 개수 출력
        print(len(queue))
    elif arr[0] == 'empty':
        # 큐가 비어있으면 1, 아니면 0을 출력
        if queue:
            print(0)
        else:
            print(1)
    elif arr[0] == 'front':
        # 가장 앞에 있는 정수 출력. 만약 큐에 들어있는 정수가 없는 경우 -1을 출력
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        # 가장 뒤에 있는 정수 출력. 만약 큐에 들어있는 정수가 없는 경우 -1을 출력
        if queue:
            print(queue[-1])
        else:
            print(-1)