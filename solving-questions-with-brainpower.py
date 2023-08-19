class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        ans = [0] * n
        max_ = -inf

        for i in range(n - 1, -1, -1):
            curr = questions[i][0]
            idx = i + questions[i][1] + 1

            if idx < n:
                curr += ans[idx]

            max_ = max(max_, curr)
            ans[i] = max_

        return max_