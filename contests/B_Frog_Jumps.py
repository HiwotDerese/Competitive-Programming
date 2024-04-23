test = int(input())

for _ in range(test):
    s = input()
    n = len(s)
    ans = 0

    left, right, count = 0, 0, 0

    while right < n:
        if s[right] == "L":
            right += 1
            count += 1

        else:
            count = 0
            right += 1
            left = right
        ans = max(ans, count)

    print(ans + 1)

