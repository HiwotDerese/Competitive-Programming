test = int(input())

for _ in range(test):
    a, b, c = map(int, input().split())

    if a + b == c:
        print("+")

    else:
        print("-")