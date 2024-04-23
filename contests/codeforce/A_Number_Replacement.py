test = int(input())

for i in range(test):
    leng = int(input())
    n = list(map(lambda a: int(a), input().split(' ')))
    s = input()

    dic = {}
    var = 0
    for i in range(leng):
        if n[i] not in dic:
            dic[n[i]] = s[i]
        elif dic[n[i]] != s[i]:
            print("NO")
            var += 1
            break
    if var == 0:
        print("YES")


