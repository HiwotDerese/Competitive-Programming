test = int(input())

for _ in range(test):

    ans = 0
    for i in range(10):
        row = list(input())

        for col in range(10):
            # print(row, col, "hereee")
            if row[col] == "X":
                min_ = min(min(i, 9 - i), min(col, 9 - col))
                ans += min_ + 1

    print(ans)


