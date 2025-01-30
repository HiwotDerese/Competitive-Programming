from collections import deque

test = int(input().strip())
ans = []

def bfs(n):
        if n == 0:
            return 0

        queue = deque([(0, 0)])  
        visited = set()
        visited.add(0)
        
        while queue:
            current, steps = queue.popleft()
            
            for move in [2, 3, -2, -3]:
                new_position = current + move
                
                if new_position == n:
                    return steps + 1
                
                if new_position not in visited:
                    visited.add(new_position)
                    queue.append((new_position, steps + 1))
    
        return -1

for _ in range(test):
    n = int(input().strip())
    ans.append(bfs(n))

for result in ans:
    print(result)
