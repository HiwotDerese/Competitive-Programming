class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordFilter:
    def __init__(self, words: List[str]):
        self.root, self.dic_ = TrieNode(), {}

        def insert(word):
            curr = self.root
            
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.is_end = True


        for idx, word in enumerate(words):
            if word not in self.dic_:
                insert(word)

            self.dic_[word] = idx

    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        pre = []

        for char in pref:
            if char not in curr.children:
                return -1

            curr = curr.children[char]

        def dfs(trie, word = ""):
            if trie.is_end:
                pre.append(pref + word )

            for char in trie.children:
                dfs(trie.children[char], word + char)

        dfs(curr)

        n, ans = len(suff), -inf
        for word in pre:
            if word[-n:] == suff:
                ans = max(ans, self.dic_[word])

        return -1 if ans < 0 else ans


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)