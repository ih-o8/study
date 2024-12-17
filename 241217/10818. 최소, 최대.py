min_num = 1000000
max_num = -1000000
n = int(input())
lst = list(map(int, input().split()))
for num in lst:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(f'{min_num} {max_num}')


# n = int(input())
# lst = list(map(int, input().split()))
# print(f'{min(lst)} {max(lst)}')