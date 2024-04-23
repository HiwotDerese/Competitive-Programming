class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if (j == len(nums2) - 1):
                    output.append(-1)
                    break
                elif ((nums1[i] == nums2[j]) and (nums2[j] < nums2[j + 1])):
                    output.append(nums2[j + 1])
                    break
                elif nums1[i] == nums2[j]:
                    output.append(-1)
                    break
        return output
                    
        