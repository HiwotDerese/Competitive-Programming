class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(2):
            if edges[0][i] in edges[1]:
                return edges[0][i]
        