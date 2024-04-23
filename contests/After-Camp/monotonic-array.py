class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_ = sorted(nums)
        rev_sorted = sorted(nums, reverse=True)

        if nums == sorted_ or nums == rev_sorted:
            return True

        return False
        
        