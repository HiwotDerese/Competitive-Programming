class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elt_sum = sum(nums)
        # print(elt_sum)
        
        leng = len(nums)
        str_arry = list(map(str, nums))
        # print(str_arry)  
        digit_sum = 0
        for i in range(leng):
            for j in range(int(len(str_arry[i]))):
                num = int(str_arry[i][j])
                digit_sum += num
                
        ans = abs(elt_sum - digit_sum)
        # print(ans)
        return ans
                
        