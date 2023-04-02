n, count = int(input()), 0

for i in range(2, n + 1):
    factorization = []
    d = 2

    while d * d <= i:
        while i % d == 0:
            factorization.append(d)
            i //= d
        d += 1

    if i > 1:
        factorization.append(i)
    
    if len(set(factorization)) == 2:
        count += 1

print(count)

