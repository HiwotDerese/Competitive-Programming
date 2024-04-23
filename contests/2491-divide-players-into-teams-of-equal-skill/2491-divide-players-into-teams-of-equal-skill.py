class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        
        ans = 0
        _sum = skill[left] + skill[right]
        
        while left < right:
            if skill[left] + skill[right] == _sum:
                prod = skill[left] * skill[right]
                ans += prod
                left += 1
                right -= 1
                
            else:
                return -1
            
        return ans
            
        