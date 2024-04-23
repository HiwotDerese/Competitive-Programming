class Solution:
    def minSteps(self, n: int) -> int:
        copy, paste, clipboard, ans = 1, 0, 0, 0
        while copy < n:
            if n % copy == 0:
                clipboard = copy
                ans += 1

            copy += clipboard
            ans += 1

        return ans