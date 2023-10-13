class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        arr = []

        for num in nums:
            curr = []
            for i in range(L-1, -1, -1):
                curr.append(num >> i & 1)

            arr.append(curr)

        nums = arr

        trie = {}
        max_xor = 0
        for num in nums:
            curr_node = trie
            xor_node = trie
            curr_xor = 0

            for bit in num:
                toggled_bit = 1 - bit

                if bit not in curr_node:
                    curr_node[bit] = {}
                    
                curr_node = curr_node[bit]
                
                if toggled_bit in xor_node:
                    xor_node = xor_node[toggled_bit]
                    curr_xor = (curr_xor << 1) | 1

                else:
                    xor_node = xor_node[bit]
                    curr_xor = curr_xor << 1

            max_xor = max(max_xor, curr_xor)
            
        
        return max_xor


        # print(nums)
        return 0



# class TrieNode:
#     def __init__(self) -> None:
#         # self.is_end = False
#         self.children = [None for _ in range(2)]
# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         max_ = len(bin(max(nums))) - 2
#         root = TrieNode()
#         ans = -inf
#         def insert(num):
#             curr = root
#             # print(curr, "rooot")

#             for bit in num:
#                 idx = int(bit)
#                 if not curr.children[idx]:
#                     curr.childr


#         n = len(nums)
#         for idx in range(n):
#             bit_rep = bin(nums[idx])[2:].zfill(max_)
#             xor = ""
#             curr = root

#             insert(bit_rep)
            
#             for i in range(max_):

#                 curr_bit = int(bit_rep[i])
#                 if curr_bit and curr.children[0]:
#                     xor += "1"
#                     curr = curr.children[0]

#                 elif (not curr_bit )and curr.children[1]:
#                     xor += "1"
#                     curr = curr.children[1]

#                 else:
#                     xor += "0"
#                     if curr_bit:
#                         curr = curr.children[1]
#                     else:
#                         curr = curr.children[0]
#             ans = max(ans, int(xor, 2))

#         return ans