arr = []
for _ in range(3):
    arr.append(input())

ans = 4

for i in range(3):
    if arr[i] != 'FizzBuzz' and arr[i] != 'Fizz' and arr[i] != 'Buzz':
        if i == 0:
            ans = int(arr[i]) + 3
            break
        elif i == 1:
            ans = int(arr[i]) + 2
            break
        else:
            ans = int(arr[i]) + 1
            break

# 15의 배수 “FizzBuzz”
# 3의 배수 “Fizz”
# 5의 배수 “Buzz”

if ans % 15 == 0:
    print('FizzBuzz')
elif ans % 3 == 0 and ans % 5 != 0:
    print('Fizz')
elif ans % 3 != 0 and ans % 5 == 0:
    print('Buzz')
else:
    print(ans)