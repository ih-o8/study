'''
현재 큐의 가장 앞에 있는 문서의 중요도
보다 높은 게 있으면, 큐의 뒤에 재배치
없으면 출력
문서가 몇 번째로 출력되는지 알아내는 문제
n, m: 문서의 개수와 알아내고자 하는 문서(0부터)
'''
from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    # 문서의 순서
    papers = deque(range(0, n))

    while queue:
        # 가장 앞에 있는 문서의 중요도와 비교
        num = queue.popleft()
        paper = papers.popleft()



