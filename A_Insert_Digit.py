test = int(input())

for i in range(test):
    n, d = map(int, input().split())
    num = input()

    for j in range(n):
        if int(num[j]) < d:
            ans = num[:j] +  str(d) + num[j:]
            break

        elif j == n - 1:
            ans = num + str(d)

    print(int(ans))