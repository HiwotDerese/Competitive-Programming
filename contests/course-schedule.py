class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        incoming = {}
        for i in range(numCourses):
            incoming[i] = 0

        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            incoming[pair[0]] += 1

        queue = deque()
        count = 0

        for course in incoming:
            if incoming[course] == 0:
                queue.append(course)

        while queue:
            c = queue.popleft()
            count += 1

            for neighbor in graph[c]:
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                    
        if count == numCourses:
            return True