class Solution:        
            
    def PredictTheWinner(self, nums: List[int]) -> bool:

        leng = len(nums)

        score1 = self.play(0, (leng - 1), nums, 1)

        score2 = sum(nums) - score1
        
        if score1 >= score2:
            
            return True

        return False
    
    
    def play(self, left, right, nums, turn):
        if left > right:
            return 0

        choice1 = self.play(left + 1, right, nums, -turn)
        choice2 = self.play(left, right - 1, nums, -turn)
        
        if turn == 1:
            
            return max(choice1 + nums[left], choice2 + nums[right])
            
        else:
            
            return min(choice1, choice2)
        
        
    
    
    