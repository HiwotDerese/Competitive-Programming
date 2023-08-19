from collections import defaultdict


test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    flag, ans = 1, 0

    mod = defaultdict(list)

    for i in range(n):
        num = arr[i] % 2
        mod[num].append(arr[i])


    for i in mod:
        if len(mod[i]) % 2 != 0:
            flag = 0
            print(-1)
            break
        else:
            ans += len(mod[i]) // 2

    if flag:
        print(ans)

    
