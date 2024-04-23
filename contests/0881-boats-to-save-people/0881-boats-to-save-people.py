class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leng = len(people)
        left = 0
        right = leng - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                ans += 1
            else:
                right -= 1
                ans += 1
                    
        return ans
                
        