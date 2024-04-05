test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    a = sorted(arr)
    unique = list(set(arr))

    if a == arr and len(unique) == n:
        print("YES")

    else:
        print("NO"	)