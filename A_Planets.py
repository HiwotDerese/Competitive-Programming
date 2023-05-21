from collections import Counter


t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))

    dic = Counter(arr)
    ans = 0
    for i in dic:
        if dic[i] < c:
            ans += dic[i]

        else:
            ans += c
    print(ans)