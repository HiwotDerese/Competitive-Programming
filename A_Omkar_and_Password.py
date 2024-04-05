test = int(input())

for _ in range(test):
    n = int(input())
    s = input().split()
    
    unique = set(s)

    if len(unique) == 1:
        print(n)

    else:
        print(1)