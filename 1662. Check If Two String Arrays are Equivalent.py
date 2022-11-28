class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        firstWord = ""
        secondWord = ""
        maxm = max(len(word1), len(word2))
        for i in range(maxm):
            if i < len(word1):
                firstWord += word1[i]
            if i < len(word2):
                secondWord += word2[i]
        if firstWord == secondWord:
            return True
        return False
                
