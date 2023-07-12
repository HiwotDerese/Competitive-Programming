class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_ = values[0] + values[1] - 1
        diff = max(values[0] - 2, values[1] - 1)

        for idx in range(2, len(values)):
            max_ = max(max_, values[idx] + diff)
            diff = max(diff - 1, values[idx] - 1)

        return max_
        