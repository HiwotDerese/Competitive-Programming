test = int(input())
# print(100 ^ 0 , "f")

for i in range(test):
    leng = int(input())
    original = list(map(int, input().split()))
    
    # print(arr)
    for i in range(leng):
        arr = original
        x = arr[i]
        arr.pop(i)
        num = arr[0]
        for j in range(1, len(arr)):
            # print(num, arr[j])
            num = num ^ arr[j]

        if num == x:
            print(x)
            break
        
        arr.insert(x, i)

