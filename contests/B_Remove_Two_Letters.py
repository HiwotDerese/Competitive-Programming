test = int(input())

for _ in range(test):
    n = int(input())
    s = input()

    pre = s[:2]
    left, count = 1, 0

    for idx in range(3, n + 1):
        curr = s[left: idx]
        if curr == pre or curr == pre[::-1]:
            count += 1

        pre = curr
        left += 1

    print(n - count - 1)



