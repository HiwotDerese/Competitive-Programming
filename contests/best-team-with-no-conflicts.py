class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        comb, n = [], len(scores)
        dp = []

        for idx in range(n):
            comb.append((ages[idx], scores[idx]))
        comb.sort()

        for idx in range(n):
            dp.append(comb[idx][1])

        for i in range(1, n):
            for j in range(i):
                if comb[j][1] <= comb[i][1]:
                    dp[i] = max(dp[i], dp[j] + comb[i][1])

        return max(dp)





        # dp = defaultdict(int)

        
        # def dfs(idx, score, prev_idx):
        #     if idx >= n:
        #         return score

        #     if (idx, score, prev_idx) in dp:
        #         return dp[(idx, score, prev_idx)]

        #     if prev_idx != -1 and comb[idx][1] < comb[prev_idx][1]:
        #         choice1 = score

        #     else:
        #         choice1 = dfs(idx  + 1, score + comb[idx][1], idx)

        #     choice2 =  dfs(idx  + 1, score, prev_idx)

        #     dp[(idx, score, prev_idx)] = max(choice1, choice2)

        #     return dp[(idx, score, prev_idx)]

        # return dfs(0, 0, -1)