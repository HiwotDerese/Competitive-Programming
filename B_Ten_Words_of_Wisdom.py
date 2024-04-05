test = int(input())

for _ in range(test):
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > ans:
            ans = b
            idx = i + 1

    print(idx)
