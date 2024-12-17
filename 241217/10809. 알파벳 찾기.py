# ord('a') == 97

alphabet = [-1] * 26

string = input()
for i in range(len(string)):
    if alphabet[ord(string[i]) - 97] == -1:
        alphabet[ord(string[i]) - 97] = i

print(*alphabet)