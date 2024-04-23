class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # n, m = len(haystack), len(needle)
        # lps = [0] * m
        # prev, curr = 0, 1
        # while curr < m:
        #     if needle[prev] == needle[curr]:
        #         lps[curr] += prev + 1
        #         prev += 1
        #         curr += 1

        #     elif prev == 0:
        #         curr += 1

        #     else:
        #         prev = lps[prev - 1]


        # si, pi = 0, 0
        # # print(lps)
        # while si < n:
        #     if haystack[si] == needle[pi]:
        #         si += 1
        #         pi += 1

        #     elif pi == 0:
        #         si += 1

        #     else:
        #         pi = lps[pi - 1]

        #     if pi >= m:
        #         return si - pi

        # return -1





        left, right, n, m = 0, 0, len(haystack), len(needle)
        if n < m:
            return -1

        dic_ = {}

        for idx in range(n):
            dic_[idx] = pow(27, idx)

        # a = 27
        pattern, window = 0, 0

        c = m - 1
        for idx in range(m):
            # print(c, needle[idx], idx)
            pattern += (ord(needle[idx]) - 97 + 1) * dic_[c]
            window += (ord(haystack[idx]) - 97 + 1) * dic_[c]
            c -= 1

        print(pattern, window)

        

        left = 0
        if pattern == window:
                return left

        for right in range(m, n):

            window -= ((ord(haystack[left]) - 97 + 1) * dic_[m - 1])
            window = (window * 27) + ord(haystack[right]) - 97 + 1
            left += 1

            if pattern == window:
                return left

        return -1





        # print(key_)



        # if m > n:
        #     return -1

        # for i in range(n):
        #     l = i
        #     print(j, i, m)
        #     while j < i + m and j < n:
        #         if haystack[l] == needle[j]:
        #             l += 1
        #             j += 1
        #             if j == i + m - 1:
        #                 return i

        #         else:
        #             i += 1
        #             j = i
        #             break

        # return -1