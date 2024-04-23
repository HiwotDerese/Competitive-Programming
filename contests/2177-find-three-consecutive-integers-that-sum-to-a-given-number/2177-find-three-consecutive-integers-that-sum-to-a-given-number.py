class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num % 3 != 0:
            return []
        
        ans = []
        num = num // 3
        ans.append(num - 1)
        ans.append(num)
        ans.append(num + 1)
        
        return ans
        
        