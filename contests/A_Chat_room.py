s = input()
n = len(s)

if n < 5:
    print("NO")

else:
    t = "hello"
    j = 0
    for i in range(n):
        if s[i] == t[j]:
            j += 1

        if j == 5:
            print("YES")
            exit()

    print("NO")


