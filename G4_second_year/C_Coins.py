from cmath import inf
test = int(input())

for _ in range(test):
    coins = int(input())

    if coins < 3:
        print(coins)

    else:
        three = coins % 3
        five = coins % 5
        num = coins
        f = False
        comb = inf
        while num > 3:
            num -= 3
            if num % 3 == 0 or num % 5 == 0:
                f = True
                comb = 0
                break

        if not f:
            while num > 5:
                num -= 5
                if num % 3 == 0 or num % 5 == 0:
                    comb = 0
                    break

        print(min(three, five, comb))