import math

class Solution:
    def maxScore(self, nums) -> int:
        gcds = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                gcds.append((math.gcd(nums[i], nums[j]), i, j))
        gcds.sort()
        print(gcds)
        self.res = 0
        used = [0] * (len(nums))

        def backtrack(op, idx, cur_score) -> None:
        
            if op == 0:
                self.res = max(self.res, cur_score)
            elif idx >= 0:
                g, i, j = gcds[idx]
                if g == 1:
                    self.res = max(self.res, (op + 1) * op // 2 + cur_score)
                    return
                if not used[i] and not used[j]:  # take the current i, j
                    used[i] = used[j] = 1
                    backtrack(op - 1, idx - 1, cur_score + op * g)
                    used[i] = used[j] = 0
                # or skip                print(i, j)
                backtrack(op, idx - 1, cur_score)

        backtrack(len(nums) // 2, len(gcds) - 1, 0)
        return self.res
sol = Solution()
sol.maxScore([1,2,3,4,5,6])