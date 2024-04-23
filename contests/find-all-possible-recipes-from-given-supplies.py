class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        ans, n = [], len(recipes)
        indegree = {}

        for i in range(n):
            indegree[recipes[i]] = 0

        for i in range(n):
            m = len(ingredients[i])

            for j in range(m):
                u = recipes[i]
                v = ingredients[i][j]

                graph[v].append(u)
                indegree[u] += 1

        # print(graph, indegree)
        queue = deque(supplies)

        while queue:
            m = queue.popleft()
            if m in recipes:
                ans.append(m)

            for neighbor in graph[m]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return ans