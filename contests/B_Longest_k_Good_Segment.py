n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

left, unique = 0, []

for right in range(len(arr)):
    if len(unique) > k:
        unique
