class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in range(len(accounts)):
            wealth = sum(accounts[i])
            arr.append(wealth)
        return max(arr)