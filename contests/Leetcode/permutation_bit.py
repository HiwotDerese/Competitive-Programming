def permutation(nums, index, permutations, i, ans):
        leng = len(nums)
        # print(permutations)
        if permutations and len(permutations) == leng:
            # print(permutations)
            ans.append(permutations.copy())
            return
        
        for j in range(leng):
            # print(j, permutations)
            if i == j:
                continue
                
            m = index & (1 << j) == 0
            if m:
                permutations.append(nums[j])
                permutation(nums, index + 2 ** j, permutations, i, ans)
                permutations.pop()
                
        
        
def permute(nums):
    ans, leng = [], len(nums)
    for i in range(leng):
        # print(i, self.ans)
        permutation(nums, 2 ** i, [nums[i]], i, ans)
        
    return ans

print(permute([1,2,3]))


