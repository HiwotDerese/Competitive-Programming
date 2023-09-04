from copy import deepcopy

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        solved = [[1,2,3],[4,5,0]]

        if board == solved:
            return 0

        for row in range(2):
            for col in range(3):
                if board[row][col] == 0:
                    row1, col1 = row, col
                    break

        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque([(row1, col1, board)])
        visited = set()
        moves = 0

        while queue:
            leng = len(queue)

            for _ in range(leng):
                row, col, state = queue.popleft()

                for dx, dy in directions:
                    newx = row + dx
                    newy = col + dy
                    new_state = deepcopy(state)

                    if 0 <= newx < 2 and 0 <= newy < 3 and tuple(map(tuple, new_state)) not in visited:
                        new_state[row][col], new_state[newx][newy] = new_state[newx][newy], new_state[row][col]
                        queue.append((newx, newy, new_state))
                        
                        if new_state == solved:
                            return moves + 1

                visited.add(tuple(map(tuple, state)))

            moves += 1

        return -1