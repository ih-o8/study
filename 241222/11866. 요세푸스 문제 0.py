from collections import deque

n, k = map(int, input().split())

arr = deque([n for n in range(1, n + 1)])
ans = []
while len(arr) >= 2:
    turn = k - 1
    while turn:
        # 한 사람씩 뒤로 보내기
        arr.append(arr.popleft())
        turn -= 1
    ans.append(arr.popleft())
ans.append(arr.popleft())

ans = list(map(str, ans))
print(f'<{", ".join(ans)}>')