test = int(input())
cards = list(map(int, input().split()))
l = 0
r = test-1
cnt = 1
wub = 0
hen = 0
while l <= r:
    if cnt%2 == 0:
        if cards[l] >= cards[r]:
            hen += cards[l]
            l += 1
        else:
            hen += cards[r]
            r -= 1
    else:
        if cards[l] >= cards[r]:
            wub += cards[l]
            l += 1
        else:
            wub += cards[r]
            r -= 1
    cnt += 1
        

print(str(wub) + " " + str(hen))



