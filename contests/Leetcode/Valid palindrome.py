class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in range(len(s)):
            if s[i].isupper():
                # s[i] = s[i].lower()
                word += s[i].lower()
            if s[i].islower():
                word += s[i]
            if s[i].isdigit():
                word += s[i]
        print(word)
        # if len(word) == 1:
        #     return False
        j = len(word) - 1
        for i in range(len(word) // 2):
            print(word[i])
            if word[i] != word[j]:
                return False
            j -= 1
        return True
            
            

            