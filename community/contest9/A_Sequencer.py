t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = []

    for i in range(n // 2):
        result.append(str(a[i]))
        result.append(str(a[n - 1 - i]))

    if n % 2 == 1:
        result.append(str(a[n // 2]))
        
    print(" ".join(result))
