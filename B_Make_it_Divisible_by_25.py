from collections import defaultdict


test = int(input())

for _ in range(test):
    num = input()
    n = len(num)
    ans1 = 0
    ans2 = 0
    idx = n - 1
    # print(idx, 'start')

    while idx >= 0 and (num[idx] != '0' and num[idx] != '5'):
        # print(num[idx])
        ans1 += 1
        idx -= 1

    possible = {0: ['0', '5'], 5: ['2', '7']}
    for j in range(idx - 1, -1, -1):
        if num[idx] == '0':
            if num[j] in possible[0]:
                if len(possible[0]) == 4:
                    ans2 += 1
                break
            elif num[j] == '5':
                possible[0].append('2')
                possible[0].append('7')
            else:
                if num[j] == '0' or num[j] == '5':
                    ans2 += 2
                else:
                    ans2 += 1

        if num[idx] == '5':
            if num[j] in possible[5]:
                # print('sss')
                if len(possible[5]) == 4:
                    ans2 += 1
                break

            elif num[j] == '0':
                possible[5].append('0')
                possible[5].append('5')

            else:
                ans2 += 1

    print(ans1 + ans2)

        


