class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ans = []

        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])

        def dfs(course, pre):
            if pre in graph[course]:
                return True
            visited.add(course)

            for node in graph[course]:
                if node not in visited:
                    if dfs(node, pre):
                        return True
                    
            return False

        for i in range(len(queries)):
            visited = set()

            if dfs(queries[i][0], queries[i][1]):
                ans.append(True)

            else:
                ans.append(False)

        return ans