class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = Counter(nums)

        for num in dic:
            if dic[num] == 1:
                return num
