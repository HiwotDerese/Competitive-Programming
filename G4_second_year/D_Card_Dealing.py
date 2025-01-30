n = int(input())

for _ in range(n):
    cards = int(input())
    alice = 0
    target = 1
    n = cards
    f = False


    while n > 0:

        if target >= n:
            if f:
                alice += n
        
        else:
            if f:
                alice += target
                if target + 1 > n:
                    alice += n

                else:
                    alice += target + 1



    print(alice, cards - alice)

