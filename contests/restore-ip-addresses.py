class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(address, dots, idx):
            if dots == 3:
                if len(s[idx:]) == 1 or (s[idx:][0] != '0' and int(s[idx:]) <= 255):
                    ans.append(address + s[idx:])
                return

            for i in range(idx + 1, min(len(s), idx + 4)):
                if len(s[idx:i]) == 1 or (s[idx:i][0] != '0' and int(s[idx:i]) <= 255):
                    dfs(address + s[idx:i] + '.', dots + 1, i)
        
        dfs('', 0, 0)
        
        return ans