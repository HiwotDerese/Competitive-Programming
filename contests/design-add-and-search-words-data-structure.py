class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            idx = ord(char) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.is_end = True
        
    def search(self, word: str) -> bool:

        def dfs(root, idx):

            if idx == len(word):
                return root.is_end

            if word[idx] == ".":
                for child in root.children:
                    if child and dfs(child, idx + 1):
                        return True

            else:
                key = ord(word[idx]) - 97
                if root.children[key] and dfs(root.children[key], idx + 1):
                    return True

                return False

        return dfs(self.root, 0)



        # arr = [self.root]
        # for char in word:
        #     new = []
        #     idx = ord(char) - 97

        #     for child in arr:
        #         if child:
        #             if char == ".":
        #                 new += [c for c in child.children if c]
                
        #             elif child.children[idx]:
        #                 new.append(child.children[idx])

        #     if not new:
        #         return False

        #     arr = new
        # if arr[0].is_end:
        #     return True        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)