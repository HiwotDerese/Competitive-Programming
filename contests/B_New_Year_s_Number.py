test = int(input())

for _ in range(test):
    n = int(input())
    if n % 2020 == 0 or n % 2021 == 0:
        print("YES")
    else:
        if n % 2020 <= n // 2021:
            print("YES")
        else:
            print("NO")

