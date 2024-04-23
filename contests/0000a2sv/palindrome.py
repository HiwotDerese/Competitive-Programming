class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            print("why")
            return False
        reversedX = 0
        num = x
        while num > 0:
            reversedX = (reversedX * 10) + num % 10
            num = num // 10
        if reversedX == x:
            return True 
        else:
            print("why")
            return False

        