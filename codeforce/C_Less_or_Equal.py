n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

if m == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif n == m or arr[m-1] != arr[m]:
    print(arr[m-1])
else:
    print(-1)
    


