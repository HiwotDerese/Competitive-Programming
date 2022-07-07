class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lis = []
        output = []
        dis_bet = sqrt((points[0][0] ** 2) + (points[0][1] ** 2))
        x = points[0][0]
        y = points[0][1]
        for i in range(len(points)):
            distance = sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
            if distance < dis_bet:
                dis_bet = distance
                x = points[i][0]
                y = points[i][1]
            elif (i > 0): 
                if distance == dis_bet:
                    new = []
                    new.insert(0, points[i][0])
                    new.insert(1, points[i][1])
                    lis.append(new)
        output.insert(0, x)
        output.insert(1, y)
        lis.append(output)
        return lis
            # print(output)
        