class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def index(num):
            row = n - 1 - (num - 1) // n
            col = (num - 1) % n
            if row % 2 == n % 2:
                return row, n - 1 - col
            else:
                return row, col

        ans = 0
        queue = deque([1])
        visited = set([1])

        while queue:
            for _ in range(len(queue)):
                num = queue.popleft()

                if num == n ** 2:
                    return ans

                for i in range(num + 1, min(num + 7, n ** 2 + 1)):
                    row, col = index(i)
                    if board[row][col] != -1:
                        i = board[row][col]
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)

            ans += 1

        return -1