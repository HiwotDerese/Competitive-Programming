test = int(input())

for i in range(test):
    n,m  = list(map(int, input().split()))
    arr = input()
    ans = [0] * n
    s = []

    for iter in range(m):
        for i in range(n):
            
            if s and s[-1] == "0":
                if arr[i] == "1":
                    ans[i] = 1
                    ans[i - 1] = 1
                    s.pop()
                    s.append(str(arr[i]))

            elif s and s[-1] == "1":
                if arr[i] == "1":
                    ans[i] = 1
                else:
                    if (i + 1) < n:
                        if arr[i + 1] == "1":
                            ans[i] = 0
                        else:
                            ans[i] = 1
                            s.pop()
                            s.append(str(arr[i]))
                    else:
                        ans[i] = 1
                        s.pop()
                        s.append(str(arr[i]))
                    
            elif arr[i] == "1":
                ans[i] = 1
                s.append(str(arr[i]))
            else:
                s.append(str(arr[i]))
        temp = []
        for i in range(n):
            temp.append(str(ans[i]))
        arr = "".join(temp)
        s = []

    for i in range(n):
        ans[i] = str(ans[i])
    ans = "".join(ans)

    print(ans)


