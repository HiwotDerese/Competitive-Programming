
class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = [None for _ in range(26)]


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            idx = ord(char) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.is_end = True

    
    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            idx = ord(char) - 97
            if not curr.children[idx]:
                return False
            
            elif curr.is_end:
                return True
            
            curr = curr.children[idx]

        return False
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            idx = ord(char) - 97
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]

        return True



    





        




