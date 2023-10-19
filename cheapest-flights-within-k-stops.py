class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for frm, to, cst in flights:
            graph[frm].append((cst,to))
        
        queue = [(0, 0, src)]
        heapq.heapify(queue)

        min_ = [(inf, inf)]*n
        min_[src] = (0,0)

        while queue:
            cost, stop, x = heapq.heappop(queue)
            if x == dst:
                return cost

            if stop <= k:
                for price, to in graph[x]:
                    if price + cost < min_[to][0]  or stop + 1 < min_[to][1]:
                        min_[to] = (price + cost, stop + 1)

                        heapq.heappush(queue, (cost + price, stop + 1, to))

        return -1