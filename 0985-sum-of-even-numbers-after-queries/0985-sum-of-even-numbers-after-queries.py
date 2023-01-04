
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        answer = []
        leng = len(nums)
        sums = 0
        for i in range(leng):
            if nums[i] % 2 == 0:
                sums += nums[i]
        
        for i in range(leng):
            index = queries[i][1]
            even = nums[index] % 2 == 0
            added = (nums[index] + queries[i][0])
            
            if even and added % 2 == 0:
                sums += queries[i][0]
                
            elif even and added % 2 != 0:
                sums -= nums[index]
                
            elif not even and added % 2 != 0:
                pass
            
            else:
                sums += added
                
            answer.append(sums)
            nums[index] += queries[i][0]
 
 
        return answer
        
        