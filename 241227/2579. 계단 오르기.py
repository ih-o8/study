# DP
from collections import deque

n = int(input())
step = [0] * (n + 1)
for i in range(1, n+1):
    step[i] = int(input())

queue = deque([(0, 0, 0)])  # 연속, 인덱스, 총합

while queue:
    cnt, idx, ans = queue.popleft()
    # 두 칸 오르기
    if cnt + 2 <= 2:
        queue.append((cnt + 2, idx + 2, ))
    # 한 칸 오르기


(1,1,10)=>(2,2,20), (2,3,15)