class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort(reverse=True)  # Sort the satisfaction values in descending order.

        n = len(satisfaction)
        pre_sum, ans = 0, 0

        for i in range(n):
            pre_sum += satisfaction[i] 

            if pre_sum >= 0:
                ans += pre_sum

            else:
                break

        return ans