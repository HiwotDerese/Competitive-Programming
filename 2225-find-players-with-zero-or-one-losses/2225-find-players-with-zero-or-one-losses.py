class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winner = {}
        loser = {}
        leng = len(matches)
        ans1 = []
        ans2 = []
        
        for i in matches:
            winner[i[0]] = winner.get(i[0], 0) + 1
            loser[i[1]] = loser.get(i[1], 0) + 1
        for i in winner:
            if i not in loser:
                ans1.append(i)
        for i in loser:
            if loser[i] == 1:
                ans2.append(i)
        ans1.sort()
        ans2.sort()
        return [ans1, ans2]
            