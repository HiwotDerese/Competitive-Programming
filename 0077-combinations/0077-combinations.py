class Solution:
    def backtrack(self, a, arr, n, k):
        
        #base case
        if len(arr) == k:
            copy = arr[::]
            self.ans.append(copy)
            return

        #loop through all candidates
        for i in range(a,n+1):
            
            #place 
            arr.append(i)
    
            #call recursive function
            self.backtrack(i+1, arr, n, k)
    
            #remove
            arr.pop()
                
    def combine(self, n, k):
        self.ans = []
        arr = []
        
        self.backtrack(1, arr, n, k)
        return self.ans
    
    
    
    
    
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
    
    
# class Solution(object):
#     def combine(self, n, k, ans = []):
#         # ans = []

#         def backtrack(a,arr):
#             if len(arr) == k:
#                 print(ans)
                
#                 ans.append(arr)
#                 return

#             for i in range(a,n+1):
#                 arr.append(i)
                
#                 backtrack(i+1,arr)
                
#                 arr.pop()

#         backtrack(1,[])
#         return ans
    
    
    
    
    
    
    
    
    
    
    
    