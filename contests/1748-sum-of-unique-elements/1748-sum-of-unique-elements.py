class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = Counter(nums)
        # print(unique)
        ans = 0
        for i in unique:
            if unique[i] == 1:
                ans += i
                
        return ans
        
        