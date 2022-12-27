# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n = input().split(' ')
arr = list( map(lambda a: int(a), input().split(' ')) )

A = set( map(lambda a: int(a), input().split(' ')) )
B = set( map(lambda a: int(a), input().split(' ')) )

ans = 0

for i in arr:
    if i in A:
        ans += 1
        
    elif i in B:
        ans -= 1
        
print(ans)


