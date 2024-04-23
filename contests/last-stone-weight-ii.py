class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_ = sum(stones)
        half = ceil(sum_ / 2)

        dp = {}
        # print(half)

        def dfs(idx, target):
            # print(idx, target)
            if idx == len(stones) or target >= half:
                return abs(target - (sum_ - target))

            if (idx, target) in dp:
                return dp[(idx, target)]

            dp[(idx, target)] = min(dfs(idx + 1, target + stones[idx]), dfs(idx + 1, target))
            return dp[(idx, target)]

        return dfs(0, 0)