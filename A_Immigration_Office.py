leng = int(input())

names = list(input().split())
# print(names)

n = int(input())

for i in range(n):
    name = input()
    # print(name)
    start, end, ans = 0, leng - 1, 0
    while start <= end:
        
        mid = (start + end) // 2
        # print(start, end, mid)
        if name < names[mid]:
            end = mid - 1
            ans = mid
        elif name > names[mid]:
            start = mid + 1
            ans = mid + 1
    print(ans)


    


