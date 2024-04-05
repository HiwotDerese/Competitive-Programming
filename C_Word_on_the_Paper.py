test = int(input())

for _ in range(test):
    ans = ""
    for _ in range(8):
        arr = list(input())

        for j in range(8):
            if arr[j] != ".":
                ans += arr[j]

    print(ans)
