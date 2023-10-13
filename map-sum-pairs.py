class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.dic_ = {}

    def insert(self, key: str, val: int) -> None:
        curr = self.root

        if key in self.dic_:
            diff = val - self.dic_[key] 
            for char in key:
                curr.children[char].count += diff
                curr = curr.children[char]

        else:
            for char in key:
                if char in curr.children:
                    curr.children[char].count += val
                else:
                    curr.children[char] = TrieNode()
                    curr.children[char].count = val

                curr = curr.children[char]

        self.dic_[key] = val

    def sum(self, prefix: str) -> int:
        curr, ans, flag = self.root, 0, True

        for char in prefix:
            if char not in curr.children:
                flag = False
                break

            ans = curr.children[char].count
            curr = curr.children[char]

        if flag:
            return ans

        return 0



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)