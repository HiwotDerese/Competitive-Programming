class Solution:
    def dfs(self, course, pre, graph, visited):
        if pre in graph[course]:
            return True
        visited.add(course)

        for node in graph[course]:
            if node not in visited:
                if self.dfs(node, pre, graph, visited):
                    return True
                
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ans = []

        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])

        for i in range(len(queries)):
            visited = set()

            if self.dfs(queries[i][0], queries[i][1], graph, visited):
                ans.append(True)

            else:
                ans.append(False)

        return ans