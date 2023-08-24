class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans, left, right = 0, [1] * n, [1] * n

        for idx in range(1, n):
            print(idx, left[idx])
            if ratings[idx] > ratings[idx - 1]:
                left[idx] = left[idx - 1] + 1

        for idx in range(n - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                right[idx] = right[idx + 1] + 1

        for idx in range(n):
            ans += max(left[idx], right[idx])

        return ans