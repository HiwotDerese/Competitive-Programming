class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)

        if k > n:
            return False

        dic1 = {i: 0 for i in range(26)}
        dic2 = {i: 0 for i in range(26)}

        for idx in range(k):
            dic1[ord(s1[idx]) - 97] += 1
            dic2[ord(s2[idx]) - 97] += 1


        left = 0

        for right in range(k, n):
            if dic1 == dic2:
                return True

            dic2[ord(s2[left]) - 97] -= 1
            dic2[ord(s2[right]) - 97] += 1
            left += 1

        return dic1 == dic2