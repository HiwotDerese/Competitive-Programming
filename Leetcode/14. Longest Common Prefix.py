class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""
        if strs == "":
            return ans
        short_str = len(min(strs, key = len))
        for i in range(short_str):
            start = 0
            if not strs[start]:
                continue

            for j in range(len(strs) - 1):
                if strs[start][i] != strs[start+1][i]:
                    return ans

                else:
                    start += 1

            print(strs[start][i])
            ans += strs[start][i]

        return ans
