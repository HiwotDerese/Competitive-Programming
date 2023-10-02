class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        # self.is_end_of_word = False

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
                # curr.children[char] += diff
                curr = curr.children[char]

        else:
            # print(key)
            for char in key:
                if char in curr.children:
                    # print(char, curr.children)
                    curr.children[char].count += val
                    # curr.children[char] += val
                else:
                    curr.children[char] = TrieNode()
                    curr.children[char].count = val
                    # curr.children[char] = val
                # print(curr, self.root)
                # print(curr.children, curr.count)
                curr = curr.children[char]

        self.dic_[key] = val
        # print(self.root, self.dic_, key)

    def sum(self, prefix: str) -> int:
        curr, ans, flag = self.root, 0, True
        # print(curr.count, prefix)

        for char in prefix:
            # print(curr.children, "children", char)
            # print(char, prefix)
            if char not in curr.children:
                # print(char, "wrrr")
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