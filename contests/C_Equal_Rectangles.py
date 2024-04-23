test = int(input())

for i in range(test):
    n = int(input())
    sides = list(map(int, input().split()))
    leng = len(sides)
    sides.sort()
    area = sides[0] * sides[leng - 1]
    l, r, flag = 0 , leng - 1, 0
    while l < r:
        if sides[l] != sides[l +1] or sides[r] != sides[r - 1]:
            print('NO')
            flag = 1
            break
        else:
            new_area = sides[l]  * sides[r]
            if new_area != area:
                print('NO')
                flag = 1
                break
            r -= 2
            l += 2


    if flag == 0:
        print('YES')
