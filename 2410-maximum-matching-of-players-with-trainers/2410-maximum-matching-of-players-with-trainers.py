class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        lengP = len(players)
        lengT = len(trainers)
        i = 0
        j = 0
        players.sort()
        trainers.sort()
        count = 0
        
        while i < lengP and j < lengT:
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
                  
        return count