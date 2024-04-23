test = int(input())

for t in range(test):
    n, k = map(int, input().split())
    s = input()

    count = 0
    ans, left = 0, 0
    for idx in range(n):

        if s[idx] == "B":
            if count == 0:
                left = idx
                count += 1

        if idx - left + 1 == k:
            ans += count
            count = 0  
            left = idx

    print(ans + count)


