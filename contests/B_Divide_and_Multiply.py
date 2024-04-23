test = int(input())

for i in range(test):
    leng = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    left, ans = 0, sum(arr)

    for j in range(leng-1, -1, -1 ):
        if arr[j] % 2 != 0:
            right = j
            break

        if j == 0:
            right = leng - 1

    num = arr.pop(right)
    while left < len(arr):

        if arr[left] % 2 == 0:
            arr[left] = arr[left] // 2
            ans -= arr[left]
            ans += num
            num *= 2

        else:
            left += 1
    print(ans)
    