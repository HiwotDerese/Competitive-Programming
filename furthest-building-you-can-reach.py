class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff = 0
        n = len(heights)
        index, minheap = 0, []

        for i in range(n - 1):
            diff =  heights[i + 1] - heights[i]

            if diff > 0:
                heapq.heappush(minheap, diff)

            if len(minheap) > ladders:
                minm = heapq.heappop(minheap)
                bricks -= minm

            if bricks < 0:
                return i

        return n - 1