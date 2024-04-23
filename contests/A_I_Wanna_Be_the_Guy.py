n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x += y
ans = set(x)

if len(ans) == n:
    print("I become the guy.")

else:
    print("Oh, my keyboard!")




n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

p = x[0]  
q = y[0]  
x = x[1:]  
y = y[1:]  

x += y
ans = set(x)

if len(ans) == n and len(x) >= n:  
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
