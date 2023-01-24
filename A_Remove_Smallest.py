test = int(input())
for i in range(test):
    var = 0
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n-1):
        if arr[i+1] - arr[i] > 1:
            print("NO")
            var = 1 
            break

    if var == 0:
        print("YES")