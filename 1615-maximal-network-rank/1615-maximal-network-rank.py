# from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) < 2:
            return len(roads)
        
        graph = defaultdict(set)
        
        for i in range(len(roads)):
            graph[roads[i][0]].add(roads[i][1])
            graph[roads[i][1]].add(roads[i][0])
            
            
        ans = 0
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = len(graph[i]) + len(graph[j])
                
                if i in graph[j]:
                    res -= 1
                
                ans = max(ans, res)
                
                
        return ans
        # print(graph)
        # res = sorted(graph, key = lambda key: len(graph[key]))

#         pair1 = graph[res[-1]]
#         pair2 = graph[res[-2]]
#         print(pair1, pair2, graph, res)
#         ans = len(pair1) + len(pair2)

#         if res[-1] in pair2:
#             return ans - 1
        
#         return ans
        
        
        
        
        
        
        