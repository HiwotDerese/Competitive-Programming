
def applyOperations(nums):
    leng = len(nums)
    i = 0
    count = 0
    
    # for i in range(leng-1):
    while count < leng - 1:
        
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            if nums[i] == nums[i + 1]:
                nums[i] += nums[i]
                nums.pop(i + 1)
                nums.append(0)
            i += 1
            # print(nums)
        count += 1
            
    return nums


print(applyOperations([847,847,0,0,0,399,416,416,879,879,206,206,206,272]) ) 
# print(applyOperations([1,2,2,1,1,0]) ) 

