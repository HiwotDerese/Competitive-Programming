class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = m+n-1
        k = n-1
        leng = len(nums1)
        
        while j >= 0:
            left = nums1[i] if i >= 0 else -float('inf')
            right = nums2[k] if k >= 0 else -float('inf')
            
            if left >= right:
                nums1[j] = left
                j -= 1
                i -= 1
            elif left < right:
                nums1[j] = right
                j -= 1
                k -= 1
        return nums1
                
        
