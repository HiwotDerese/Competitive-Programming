class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxm = 0
        for i in range(len(sentences)):
            leng = len(sentences[i].split())
            maxm = max(maxm, leng)
        return maxm