test = int(input())
# print(test)
for i in range(test):
    if i != 0:
        space = input()
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    

    a.sort()    
    b.sort(reverse=True)
    f = False
    for j in range(n):
        if a[j] + b[j] > x:
            print("No")
            f = True
            break

    if not f:
        print("Yes")




    