test = int(input())
 
for _ in range(test):
    arr = list(input())
    point = 0
    ans = float('inf')
    dictt = {}
    
    for i in range(len(arr)):
        if arr[i] in dictt:
            dictt[arr[i]] = i

        else:
            dictt[arr[i]] = i

        if len(dictt) == 3:
            ranges = dictt.values()
            ans = min(ans, max(ranges)-min(ranges)+1)

    if ans == float('inf'):
        ans = 0

    print(ans)