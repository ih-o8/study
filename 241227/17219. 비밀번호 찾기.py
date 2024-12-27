import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = {}

for _ in range(n):
    site, password = input().split()
    lst[site] = password

for _ in range(m):
    print(lst[input().strip()])