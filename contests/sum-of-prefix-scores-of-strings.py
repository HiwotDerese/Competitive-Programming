class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        
        def insert(word):
            curr = self.root
            for char in word:
                if char in curr.children:
                    curr.children[char].count += 1

                else:
                    curr.children[char] = TrieNode()
                    curr.children[char].count = 1

                curr = curr.children[char]

        def score(word):
            curr, score = self.root, 0
            # print(word)
            for char in word:
                # print(curr, char)
                score += curr.children[char].count
                curr = curr.children[char]

            return score


        ans = []
        for word in words:
            insert(word)

        for word in words:
            ans.append(score(word))

        return ans


        # print(self.root.children["a"].children)