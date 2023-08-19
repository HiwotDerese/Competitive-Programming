n, m = map(int, input().split())
grid = []

for idx in range(n):
    nums = list(input())
    grid.append(nums)
# print(grid)
ans = ""
for row in range(n):
    for col in range(m):
        # print(row, col)

        flag = True
        for hor in range(n):
            if hor != row and grid[row][col] == grid[hor][col]:
                # print(row, col, grid[row][hor], "hor")
                flag = False
                break

        for ver in range(m):
            if ver != col and grid[row][col] == grid[row][ver]:
                # print(row, col, "ver")
                flag = False
                break

        if flag:
            ans += grid[row][col]

print(ans)
