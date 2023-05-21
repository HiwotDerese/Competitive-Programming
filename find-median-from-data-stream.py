class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []        

    def addNum(self, num: int) -> None:
        # print(self.maxheap, self.minheap, num)
        heapq.heappush(self.maxheap, -num)

    def findMedian(self) -> float:
        
        while len(self.maxheap) - len(self.minheap) > 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if self.maxheap and self.minheap and -self.maxheap[0] > self.minheap[0]:
            temp1, temp2 = -heappop(self.maxheap), -heappop(self.minheap)
            heappush(self.minheap, temp1)
            heappush(self.maxheap, temp2)

        if len(self.maxheap) - len(self.minheap) == 1:
            return -self.maxheap[0]
        
        num1 = -heapq.heappop(self.maxheap)
        num2 = heapq.heappop(self.minheap)

        ans = (num1 + num2) / 2
        heapq.heappush(self.maxheap, -num1)
        heapq.heappush(self.minheap, num2)
        # print('c', ans)
        return ans


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()