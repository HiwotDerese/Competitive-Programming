class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def combination(idx, sum_):
            if (idx, sum_) in dp:
                return dp[(idx, sum_)]

            if idx == len(coins) or sum_ > amount:
                return inf
            
            if amount == sum_:
                return 0

            dp[(idx, sum_)] = min( 1 + combination(idx, sum_ + coins[idx]), combination(idx + 1, sum_)  )

            return dp[(idx, sum_)]

        ans = combination(0, 0)

        return ans if ans < inf else -1