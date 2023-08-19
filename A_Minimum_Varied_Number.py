test = int(input())

for _ in range(test):

    num = int(input())

    if num <= 9:
        print(num)

    else:
        ans = ['9']
        base = 9
        while num - base >= int(str(ans[0])):
            base += int(ans[0]) - 1
            a = str(int(ans[0]) - 1)
            ans.insert(0, a)

        ans.insert(0, str(num - base ))

        print("".join(ans))

