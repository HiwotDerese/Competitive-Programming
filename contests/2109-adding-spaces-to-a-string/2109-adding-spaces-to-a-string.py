class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        leng = len(s)
        count = 0
        ans = ""
        for i in range(leng):
            if count < len(spaces):
                if i == spaces[count]:
                    ans += " "
                    ans += s[i]
                    count += 1
                else:
                    ans += s[i]
            else:
                ans += s[i]
        return ans