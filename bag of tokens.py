class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        while i < j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        if i == j and power >= tokens[i]:
            score += 1
        return score
            





