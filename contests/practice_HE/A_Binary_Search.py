n, k = map(int, input().split())

arr = list(map(int, input().split()))
query = list(map(int, input().split()))
n = len(arr)

for idx in range(len(query)):
    target = query[idx]
    left, right, found = 0, n - 1, False

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

        else:
            print("YES")
            found = True
            break

    if not found:
        print("NO")
        