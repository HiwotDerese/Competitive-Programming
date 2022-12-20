class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        output = []
        for i in range(len(points) - 1):
            for j in range(i+1,len(points),1):
                distance = sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
                if distance > sqrt((points[j][0] ** 2) + (points[j][1] ** 2)):
                    points[i], points[j] = points[j], points[i]
                    
        for i in range(0,k,+1):
            output.append(points[i])
        return output
               
        