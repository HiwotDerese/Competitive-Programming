# import sys
# # kth bit from the right, 1 indexed
# def kthBitTest(num : int, k : int) -> int:
#     # TODO
#     # num = num >> k
#     # if num % 2 == 0:
#     #     return 0
#     # return 1

#     # num2 = 1 << k
#     # if num2 & num != 0:
#     #     return 1
#     # return 0

#     return (num >> k) & 1

# def test():
#     assert kthBitTest(6, 2) == 1,'Ooops'
#     assert kthBitTest(3, 1) == 1, 'Ooops'
#     print('Niceee')

# test()



# import sys
# # Set the Kth bit from the right, 1 indexed
# def kthBitSet(num : int, k : int) -> int:
# 	# TODO
#     return num | 1 << k - 1


# def test():
#     assert kthBitSet(6, 1) == 7,'Ooops'
#     assert kthBitSet(3, 4) == 11, 'Ooops'
#     print('Niceee')

# test()



import sys
# turn off the kth bit from the right, 1 indexed
def turnOffKthBit(num : int, k : int) -> int:
	# TODO
    return num & (~(1<<k-1))

def test():
    assert kthBitTest(6, 1) == 6,'Ooops'
    assert kthBitTest(6, 2) == 4,'Ooops'
    assert kthBitTest(3, 4) == 3, 'Ooops'
    print('Niceee')

test()
