class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        ans = []
        heap = []

        for i in range(n):
            tasks[i].append(i)

        heapq.heapify(tasks)

        index = 0
        time = tasks[0][0]
        while tasks:
            # print(tasks, 'tasks')

            while tasks and tasks[0][0] <= time:
                task = heapq.heappop(tasks)
                heapq.heappush(heap, (task[1], task[2]))
                index += 1
            # print(heap, '1')

            if heap:
                num = heapq.heappop(heap)
                ans.append(num[-1])
                time += num[0]
            

            else:
                time = tasks[0][0]
            # print(heap, '2')

        while heap:
            ans.append(heapq.heappop(heap)[-1])

        return ans