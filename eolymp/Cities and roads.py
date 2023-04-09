n = int(input())
count = 0
for i in range(n):
    row = list(map(int, input().split()))

    for col in range(i, n):
        if row[col] == 1:
            count += 1

print(count)
