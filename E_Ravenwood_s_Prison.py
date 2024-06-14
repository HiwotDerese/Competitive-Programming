t = int(input())

for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    unique_values = set()
    
    for k in range(n):
        unique_values.add((k + a[k]) % n)
    
    if len(unique_values) < n:
        print('NO')
    else:
        print('YES')

        