class Solution:
    def maxLength(self, arr: List[str]) -> int:
        char_set = set()

        def backtrack(i):
            if i == len(arr):
                return len(char_set)

            res = 0
            c = Counter(char_set) + Counter(arr[i])

            if not max(c.values()) > 1:
                # char_set.add(arr[i])
                for c in arr[i]:
                    char_set.add(c)

                # print(char_set)
                res = backtrack(i + 1)
                # print(res, arr[i], i, "hereeee")
                for c in arr[i]:
                    char_set.remove(c)
            # print(arr[i], char_set)
            return max(res, backtrack(i + 1))
                
        return backtrack(0)