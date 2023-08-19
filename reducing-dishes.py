class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n, ans, sum_ = len(satisfaction), 0, 0
        satisfaction.sort()
        arr = []
        start = 0

        for i in range(n - 1, -1, -1):
            if sum_ + satisfaction[i] >= 0:
                arr.append(satisfaction[i])
                sum_ += satisfaction[i]
            
            else:
                break

        arr.reverse()
        arr.insert(0, 0)
        for i in range(len(arr)):
            ans += (arr[i] * i)

        return ans