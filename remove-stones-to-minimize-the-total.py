class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)

        for i in range(n):
            piles[i] = -piles[i]

        heapq.heapify(piles)

        for i in range(k):
            num = heapq.heappop(piles)
            heapq.heappush(piles, floor(num / 2))

        return(-sum(piles))