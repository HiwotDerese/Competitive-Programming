test = int(input())

for _ in range(test):
    s = input()
    word = "abc"

    count = 0
    for i in range(3):
        if word[i] != s[i]:
            count += 1

    if count < 3:
        print("YES")

    else:
        print("NO")