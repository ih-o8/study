# 스택 활용하여 배열 완성 후 총합 구하기
# 입력받을 때 값을 더하거나 빼면 굳이 반복문 활용하지 않아도 됨

import sys
input = sys.stdin.readline

s = []
ans = 0

for _ in range(int(input())):
    n = int(input())
    if n != 0:
        s.append(n)
        ans += n
    else:
        if s:
            ans -= s.pop()

print(ans)