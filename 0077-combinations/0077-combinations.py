class Solution:
                
    def combine(self, n, k):
        
        def backtrack(a, arr, n, k):
        
        #base case
            if len(arr) == k:
                copy = arr[::]
                ans.append(copy)
                return

            #loop through all candidates
            for i in range(a,n+1):

                #place 
                arr.append(i)

                #call recursive function
                backtrack(i+1, arr, n, k)

                #remove
                arr.pop()
        
        
        
        
        
        ans = []
        arr = []
        
        backtrack(1, arr, n, k)
        return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []

#         def helper(combination, start, remaining_slots):
#             if remaining_slots == 0:
#                 ans.append(combination)
                
#             else:
#                 for num in range(start, n + 1):
#                     helper(combination + [num], num + 1, remaining_slots - 1)
                    
#             # print(ans)

#         helper([], 1, k)

#         return ans

    
    
    
    
    
    
    
    
    
    
    
    