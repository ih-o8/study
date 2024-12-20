import sys
input = sys.stdin.readline
s = []

for _ in range(int(input())):
    arr = input().split()
    if arr[0] == 'push':
        # 정수를 스택에 넣는 연산
        s.append(arr[1])
    elif arr[0] == 'pop':
        # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 정수가 없는 경우 -1 출력
        if s:
            print(s.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        # 스택에 들어있는 정수의 개수
        print(len(s))
    elif arr[0] == 'empty':
        # 스택이 비어있으면 1, 아니면 0
        if s:
            print(0)
        else:
            print(1)
    elif arr[0] == 'top':
        # 스택의 가장 위에 있는 정수를 출력, 정수가 없는 경우 -1 출력
        if s:
            print(s[-1])
        else:
            print(-1)
