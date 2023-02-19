n = int(input())

arr = list(map(int, input().split()))
l = 0
r = 2*n-1
var = 0

for i in range(n):
    if sum(arr[:n]) != sum(arr[n:]):
        print(arr)
        var += 1
    else:
        arr[l], arr[r] = arr[r], arr[l]

if var == 0:
    print(-1)



    
    