class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lenWord = len(words)
        _map = {}

        for i in range(len(order)):
            _map[order[i]] = i

        for i in range(lenWord - 1):
            short_str = min(len(words[i]), len(words[i+1]))
            index = 0

            for j in range(i, short_str):
                if _map[words[i][j]] > _map[words[i+1][j]]:
                    return False
                
                elif _map[words[i][j]] < _map[words[i+1][j]]:
                    if (i+1 == lenWord -1):
                        return True

                    else:
                        continue
                
                else:
                    index += 1
        if len(words[i]) <= len(words[i+1]):
            return True

        return False

     
                     
