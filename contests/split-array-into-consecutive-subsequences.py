class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count_graph = defaultdict(list)

        for num in nums:
            end = count_graph[num-1] 
            
            if len(end) == 0:
                count = 0 
            else:
                count =  heapq.heappop(end)

            new_heap = count_graph[num]

            heapq.heappush(new_heap, count + 1)

        for value in count_graph.values():
            for length in value:
                if length < 3:

                    return False
                    
        return True