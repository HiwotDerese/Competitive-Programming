
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
            if nums[index] % 2 == 0 and (nums[index] + queries[i][0]) % 2 == 0:
                sums += queries[i][0]
                nums[index] += queries[i][0]
            elif nums[index] % 2 == 0 and (nums[index] + queries[i][0]) % 2 != 0:
                sums -= nums[index]
                nums[index] += queries[i][0]
            elif nums[index] % 2 != 0 and (nums[index] + queries[i][0]) % 2 != 0:
                nums[index] += queries[i][0]
                # sums += nums[index] + queries[i][0]
                pass
            else:
                sums += nums[index] + queries[i][0]
                nums[index] += queries[i][0]
            answer.append(sums)

                
            # print(nums)   
            # print(answer)
            
            
        return answer
        

# class Solution:
#     def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
#         answer = []
#         leng = len(nums)
        
#         for i in range(leng):
#             index = queries[i][1]
#             nums[index] += queries[i][0]
            
#             sums = 0
#             for i in range(leng):
#                 if nums[i] % 2 == 0:
#                     sums += nums[i]

#             answer.append(sums)
#         return answer
        