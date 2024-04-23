from collections import deque


test = int(input())

for i in range(test):
    grid = []
    n = int(input())
    row1 = list(map(int, input()))
    grid.append(row1)
    row2 = list(map(int, input()))
    grid.append(row2)

    visited = set((0, 0))
    queue = deque([(0, 0)])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    inbound = lambda row, col: 0 <= row < 2 and 0 <= col < n

    goal, f = (1, n -1), 0
    while queue:
        curr_level = len(queue)

        for i in range(curr_level):
            row, col = queue.popleft()

            if (row, col) == goal:
                print('YES')
                f = 1
                break
            for dx, dy in directions:
                new_x = row + dx
                new_y = col + dy

                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))

if f == 0:
    print('NO')
    




