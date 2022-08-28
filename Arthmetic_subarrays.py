class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            newArr = nums[l[i]:r[i]+1]
            newArr.sort()
            for i in range(len(newArr)-2):
                if (newArr[i]-newArr[i+1] == newArr[i+1]-newArr[i+2]):
                    if (i== len(newArr)-3):
                        ans.append(True)
                    else:
                        continue
                else:
                    ans.append(False)
                    break
            
        return ans
                    
        