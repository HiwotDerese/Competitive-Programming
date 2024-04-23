from collections import deque


n, m = map(int, input().split())
r, c = map(int, input().split())
left, right = map(int, input().split())

laby = []

for _ in range(n):
    row = list(input())
    laby.append(row)

# print(laby)

inbound = lambda x, y: x >= 0 and x < n and y >= 0 and y < n

# print(inbound(1,2))
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set([r - 1, c - 1, left, right])

queue = deque([r - 1, c - 1, left, right])

while queue:
    leng = len(queue)

    for i in range(queue):
        r, c, left, right = queue.popleft()
        








