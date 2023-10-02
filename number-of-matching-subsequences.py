class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def is_sub(word):
            idx=-1
            for ch in word:
                # print(index, "topp")
                idx = s.find(ch,idx + 1)
                # print(index, ch, word, s)
                if idx == -1:
                    return False

            return True
        
        ans = 0
        for word in words:
            if is_sub(word):
                ans += 1
        
        return ans