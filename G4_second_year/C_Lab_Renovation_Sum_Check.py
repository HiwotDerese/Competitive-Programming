n = int(input())
grid = []

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

f = True
for row in range(n):
    for col in range(n):
        if grid[row][col] != 1:
            candidates = []

            for i in range(n):
                if i != row:
                    candidates.append(grid[row][col] - grid[i][col])

            found = False
            for i in range(n):
                if i != col:
                    if grid[row][i] in candidates:
                        found = True
                        break

            if not found:
                print('No')
                f = False
                exit()

if f:
    print('Yes')

