from collections import defaultdict

test = int(input())

for _ in range(test):
    n, m = map(int, input().split())
    # print(type(n))
    board = []

    for row in range(n):
        arr = list(map(int, input().split()))
        board.append(arr)
    # print(board)

    right_sum = defaultdict(int)
    left_sum = defaultdict(int)

    for row in range(n):
        for col in range(m):
            right_sum[col - row] += board[row][col]
            left_sum[row + col] += board[row][col]

    
    ans = 0
    for row in range(n):
        for col in range(m):
            ans = max(ans, right_sum[col - row] + left_sum[row + col] - board[row][col])


    print(ans)