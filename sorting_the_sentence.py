class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()
        
        sorted = [""] * len(words)
        
        for word in words:
            index = int(word[-1])
            # word2 = word[ : len(word) -1 ]
            word2 = word[ : -1 ]
            sorted[index - 1] =  word2
        sentence = " ".join(sorted)
        return sentence