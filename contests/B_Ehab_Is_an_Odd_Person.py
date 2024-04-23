n = int(input())
arr = list(map(int, input().split()))
even, odd = 0, 0

idx = 0
while (not odd and not even) or idx < n:
    if arr[idx] % 2 == 0:
        even += 1

    else:
        odd += 1

    idx += 1

ans = sorted(arr)
if even and odd:
    print(*ans)

else:
    print(*arr)
