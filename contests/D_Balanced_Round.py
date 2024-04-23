test = int(input())

for _ in range(test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()

    min_remove = n

    for i in range(n):
        left = 0
        for j in range(i, n):
            if a[j] - a[left] > k:
                min_remove = min(min_remove, j - i)
                while a[j] - a[left] > k:
                    left += 1

    print(min_remove)

