test = int(input())

for _ in range(test):
    coins = list(map(int, input().split()))
    max_, cnt = max(coins[:3]), 0

    for i in range(3):
        cnt += max_ - coins[i]

    if cnt > coins[3]:
        print('NO')

    else:
        if (coins[3] - cnt) % 3 == 0:
            print('YES')

        else:
            print('NO')


