test = int(input())

for _ in range(test):
    n = int(input())
    box = list(map(int, input().split()))
    ans = 0
    min_ = min(box)

    for i in range(n):
        if box[i] > min_:
            ans += box[i] - min_

    print(ans)