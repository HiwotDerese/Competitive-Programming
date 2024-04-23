def uniqueSubsets(nums, ans):
    if not nums:
        return ans

    c = ans.copy()
    for i in c:
        ans.append([nums[-1]] + i)

    ans.append([nums[-1]])
    nums.pop()
    print(ans, nums)
    # print(ans)
    uniqueSubsets(nums, ans)
        
        
        
def subsets(nums):
    ans = []
    
    uniqueSubsets(nums, ans)
    
    return [[]] + ans

print(subsets([1,2,3]))