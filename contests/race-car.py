class Solution:
    def racecar(self, target: int) -> int:
        ans = 0
        queue = deque([(0, 1)])
        visited = set([0, 1])

        while queue:
            n = len(queue)
            for i in range(n):
                seq = queue.popleft()
                if seq[0] == target:
                    return ans
                
                acc = (seq[0] + seq[1], seq[1] * 2) 
                if acc[0] == target:
                    return ans + 1

                if acc not in visited and abs(acc[0] - target) < target:
                    visited.add(acc)
                    queue.append(acc)
                    

                rev = (seq[0], -1 if seq[1] > 0 else 1)
                if rev not in visited and abs(rev[0] - target) < target:
                    visited.add(rev)
                    queue.append(rev)

            ans += 1