class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        graph = defaultdict(list)
        dic, ans, incoming = {}, [], [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            incoming[edge[0]] += 1
            incoming[edge[1]] += 1

        queue = deque()
        # add all leaf nodes
        for i in range(len(incoming)):
            if incoming[i] == 1:
                queue.append(i)

        # untill we get the center
        while n > 2:
            # print(queue)
            leng = len(queue)

            for i in range(leng):
                num = queue.popleft()
                n -= 1
                for neighbor in graph[num]:
                    incoming[neighbor] -= 1
                    
                    if incoming[neighbor] == 1:
                        queue.append(neighbor)

        return queue