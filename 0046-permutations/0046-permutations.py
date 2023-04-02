class Solution:
    
    def permutation(self, nums, index, permutations, i):
        leng = len(nums)
        # print(permutations)
        if permutations and len(permutations) == leng:
            # print(permutations)
            self.ans.append(permutations.copy())
            return
        
        for j in range(leng):
            # print(j, permutations)
            if i == j:
                continue
                
            m = index & (1 << j) == 0
            if m:
                permutations.append(nums[j])
                self.permutation(nums, index + 2 ** j, permutations, i)
                permutations.pop()
                
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans, leng = [], len(nums)
        for i in range(leng):
            # print(i, self.ans)
            self.permutation(nums, 2 ** i, [nums[i]], i)
            
        return self.ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ans = []
        # if len(nums) == 1:
        #     return [nums[:]]
        # for i in range(len(nums)):
        #     print(i, "i")
        #     print("loop")
        #     n = nums.pop(0)
        #     # print("n")
        #     print("ffff")
        #     perms = self.permute(nums)
        #     print(perms, "ffff")
        #     for i in range(len(perms)):
        #         print("loop2")
        #         perms[i].insert(-1, n)
        #         print(perms, "in")
        #     print(perms, "sssss")
        #     ans.extend(perms)
        #     nums.append(n)
        #     print(nums,"nums")
        # return ans 
            
