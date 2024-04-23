test = int(input())

for i in range(test):
    wt, et, ef = list(map(int, input().split()))
    choice1 = wt * 4
    choice2 = (ef * et) + (et * 4)
    choice3 = (wt * ef) + (4 - ef) * et

    print(min(choice1, choice2, choice3))