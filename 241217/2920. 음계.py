# lst = list(map(int, input().split()))
#
# if lst == [1, 2, 3, 4, 5, 6, 7, 8]:
#     print('ascending')
# elif lst == [8, 7, 6, 5, 4, 3, 2, 1]:
#     print('descending')
# else:
#     print('mixed')


lst = list(map(int, input().split()))

if lst == list(range(1, 9)):
    print('ascending')
elif lst == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')