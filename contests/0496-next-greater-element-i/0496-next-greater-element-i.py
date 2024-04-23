class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        output = []
        for i in range(len(nums1)):
            j = 0
            while nums1[i] != nums2[j]:
                j += 1
            
            j += 1
            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    output.append(nums2[j])
                    break 
                j += 1
            if j >= len(nums2):
                output.append(-1)
                
        return output
                    
        