class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        ans = float('inf')
        leng = len(points)
        minm = float('inf')
        
        for i in range(leng):
            x1 = points[i][0]
            y1 = points[i][1]
            
            if x == x1 or y == y1:
                distance = abs((x - x1)) + abs((y - y1))
                
                if distance < minm:
                    ans = i
                    minm = distance
            else:
                continue
                    
        return -1 if ans == float('inf') else ans
                    
        