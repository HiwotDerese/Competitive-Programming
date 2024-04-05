test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    dic = {}    
    for i in range(n):
        if arr[i] - i not in dic:
            dic[arr[i] - i] = 1
        else:
            dic[arr[i] - i] += 1
            
    ans = 0
    print(dic)
    for key in dic:
        print(key, dic[key] * (dic[key] - 1) // 2)
        ans += dic[key] * (dic[key] - 1) // 2
    print(ans)

