# 스택

# for _ in range(int(input())):
#     s = []
#     ans = 'NO'
#     string = input()
#     for i in range(len(string)):
#         if string[i] == '(':
#             s.append('(')
#         elif string[i] == ')':
#             if len(s) >= 1:
#                 if i == len(string) - 1 and len(s) == 1:
#                     ans = 'YES'
#                     break
#                 s.pop()
#             else:
#                 break
#     print(ans)

for _ in range(int(input())):
    s = 0
    ans = 'NO'
    string = input()
    for i in range(len(string)):
        if string[i] == '(':
            s += 1
        elif string[i] == ')':
            if s >= 1:
                if i == len(string) - 1 and s == 1:
                    ans = 'YES'
                    break
                s -= 1
            else:
                break
    print(ans)