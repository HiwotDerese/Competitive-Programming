class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = {}
        ans = []

        for i in range(n):
            incoming[i] = 0
            ans.append([])

        for edge in edges:
            graph[edge[0]].append(edge[1])
            incoming[edge[1]] += 1

        queue = deque()

        for i in incoming:
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            parent = queue.popleft()

            for child in graph[parent]:
                ans[child].append(parent)
                ans[child] = sorted(list(set(ans[child] + ans[parent])))
                incoming[child] -= 1
                
                if incoming[child] == 0:
                    queue.append(child)

        return ans