from cmath import inf

test = int(input())




# class TrieNode:
#     def __init__(self) -> None:
#         # self.is_end = False
#         self.children = [None for _ in range(2)]

# def insert(num):
#     curr = root
#     # print(curr, "rooot")

#     for bit in num:
#         idx = int(bit)
#         if not curr.children[idx]:
#             curr.children[idx] = TrieNode()

#         curr = curr.children[idx]


for _ in range(test):
    n = int(input())
    nums = list(map(int, input().split()))
    max_ = len(bin(max(nums))) - 2

    arr = []
    for num in nums:
        curr = []
        # print(num)
        for i in range(L-1, -1, -1):
            curr.append(num >> i & 1)

        arr.append(curr)

    nums = arr
    # print(nums)
    # nums = [[num >> i & 1 for i in range(L-1, -1, -1)] for num in nums]
    trie = {}
    max_xor = 0
    for num in nums:
        curr_node = trie
        xor_node = trie
        curr_xor = 0
        print(num)
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
        print(max_xor)
        
    print(max_xor)

#     # print(max_,max(nums), "maxx")
#     root = TrieNode()
#     ans = -inf

#     for idx in range(n):
#         # print(idx, nums)
#         bit_rep = bin(nums[idx])[2:].zfill(max_)
#         # print(bit_rep)
#         xor = ""
#         curr = root

#         # print(curr, "curr")
#         insert(bit_rep)
        
#         for i in range(max_):

#             curr_bit = int(bit_rep[i])
#             # print(curr_bit, "currr")
#             if curr_bit and curr.children[0]:
#                 # print("aaaa")
#                 xor += "1"
#                 curr = curr.children[0]

#             elif (not curr_bit )and curr.children[1]:
#                 # print("bbb", i, bit_rep, curr_bit)
#                 xor += "1"
#                 curr = curr.children[1]

#             else:
#                 # print("ccc", i, bit_rep)
#                 xor += "0"
#                 if curr_bit:
#                     # if curr.children[1]:
#                     #     curr = curr.children[1]
#                     # curr.children[1] = TrieNode()
#                     curr = curr.children[1]
#                 else:
#                     # curr.children[0] = TrieNode()
#                     curr = curr.children[0]
#         # print(bit_rep, xor)
#         # xor = "0b" + xor
#         # print(xor)
#         # print(bin(5), "hereeee")
#         # a = int(xor, 2)
#         # print(xor, "xorr******************")
#         ans = max(ans, int(xor, 2))
#         # print(bit_rep)

#     print(ans)

