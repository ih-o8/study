def carculator(a, b):
    return (a + b) * (a - b)

a, b = map(int, input().split())
print(carculator(a, b))