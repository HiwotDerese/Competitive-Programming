from collections import defaultdict
n = int(input())

for i in range(n):
    row = list(map(int, input().split()))
    ans = []

    for j in range(len(row)):
        if row[j] == 1:
            ans.append(j + 1)

    print(len(ans), *ans)
