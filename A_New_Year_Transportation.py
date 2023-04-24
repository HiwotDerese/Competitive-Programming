n, t = list(map(int, input().split()))

a = list(map(int, input().split()))

count, index, f = 0, 0, 0
i = 0
while i < (len(a)):

    count += a[i]
    i = count
    # print(index, i)
    if i == t - 1:
        print("YES")
        break


    if i > t - 1:
        print("NO")
        break
