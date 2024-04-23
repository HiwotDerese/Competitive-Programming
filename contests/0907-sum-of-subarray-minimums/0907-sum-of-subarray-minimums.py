class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr, ans, stk = [0] + arr, 0, [0]
        leng = len(arr)
        res = [0]*leng

        for right in range(leng):
#             find the previous minimum value
            while arr[stk[-1]] > arr[right]:
                stk.pop()
                
            res[right] = res[stk[-1]] + (right - stk[-1])* arr[right]
            
            ans += res[right]
            
            stk.append(right)
            
        ans = ans % 1000000007
        
        return ans


                
                
            
            
        