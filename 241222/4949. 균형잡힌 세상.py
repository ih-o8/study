import sys
input = sys.stdin.readline

while True:
    string = input().strip('\n')

    if string == '.':
        break

    s = []
    ans = 'yes'
    for word in string:
        if word == '(' or word == '[':
            s.append(word)
        elif word == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                s.append(')')
                break
        elif word == ']':
            if s and s[-1] == '[':
                s.pop()
            else:
                s.append(']')
                break
    if s:
        ans = 'no'
    else:
        ans = 'yes'
    print(ans)