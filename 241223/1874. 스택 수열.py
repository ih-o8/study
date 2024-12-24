n = int(input())
s = []
start = 1
ans = []
tf = True

for i in range(n):
    num = int(input())
    if i == 0 or num >= start:
        for j in range(start, num + 1):
            s.append(j)
            ans.append('+')
        start = num + 1
        s.pop()
        ans.append('-')
    elif num < start:
        if not s:
            tf = False
            break
        last = s.pop()
        if last != num:
            tf = False
            break
        ans.append('-')

if tf:
    for word in ans:
        print(word)
else:
    print('NO')