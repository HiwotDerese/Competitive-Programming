recipe = input()
available = list(map(int, input().split()))
price = list(map(int, input().split()))
money = int(input())
dic, ans, flag = {'B': 0, 'S': 0, 'C': 0}, 0, 0

for i in recipe:
    dic[i] += 1

while available[0] or available[1] or available[2]:
    if dic['B'] <= available[0]:
        available[0] -= dic['B']
    else:
        if money >= dic['B'] * price[0]:
            money -= dic['B'] * price[0]
        else:
            flag = 1

    if dic['S'] <= available[1]:
        available[1] -= dic['S']
    else:
        if money >= dic['S'] * price[1]:
            money -= dic['S'] * price[1]
        else:
            flag = 1

    if dic['C'] <= available[2]:
        available[2] -= dic['C']
    else:
        if money >= dic['C'] * price[2]:
            money -= dic['C'] * price[2]
        else:
            flag = 1

    if flag == 1:
        break
    else:
        ans += 1

if money:
    total = (dic['B'] * price[0]) + (dic['S'] * price[1]) + (dic['C'] * price[2])
    ans += money // total

print(ans)

