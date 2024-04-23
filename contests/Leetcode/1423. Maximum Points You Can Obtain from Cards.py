class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # if k == len(cardPoints):
        #     return sum(cardPoints)
        maxm = sum(cardPoints[:k])
        left = k - 1
        right = len(cardPoints) - 1
        Sum = maxm
        # print(Sum)
        while left >= 0:
            Sum = Sum - cardPoints[left] + cardPoints[right]
            # print(Sum)
            maxm = max(maxm, Sum)
            left -= 1
            right -= 1
        return maxm
     

