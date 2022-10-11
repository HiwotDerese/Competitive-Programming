class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashT = {}
        ans = []
        prev = 0
        for i in range(len(s)):
            hashT[s[i]] = i
        size = hashT[s[0]]
        for i in range(len(s)):
            if hashT[s[i]] == size and i == size:
                ans.append(size + 1 - prev)
                prev = i + 1
            elif hashT[s[i]] > size:
                size = hashT[s[i]]
                if i == len(s) - 1 or i == size:
                    ans.append(size + 1 - prev)
                    prev = i + 1

        return ans
