class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        destination, ans = set(), []
        
        for i in range(len(edges)):
            destination.add(edges[i][1])
            
        for i in range(n):
            if i not in destination:
                ans.append(i)
                
        return ans
        