for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = [list(range(1, n + 1))]+[[1] * n] * k

    for i in range(1, k + 1):
        for j in range(1, n):
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

    print(arr[k][n - 1])