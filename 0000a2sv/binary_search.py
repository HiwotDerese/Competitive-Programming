# """
# Beginner Python Project - Binary Search Implementation by Kylie Ying

# YouTube Kylie Ying: https://www.youtube.com/ycubed 
# Twitch KylieYing: https://www.twitch.tv/kylieying 
# Twitter @kylieyying: https://twitter.com/kylieyying 
# Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
# Website: https://www.kylieying.com
# Github: https://www.github.com/kying18 
# Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
# """

# import random
# import time

# # Implementation of binary search algorithm!!

# # We will prove that binary search is faster than naive search!


# # Essence of binary search: d0
# # If you have a sorted list and you want to search this array for something,
# # You could go through each item in the list and ask, is this equal to what we're looking for?
# # But we can make this *faster* by leveraging the fact that our array is sorted!
# # Binary search ~ O(log(n)), naive search ~ O(n)

# # In these two examples, l is a list in ascending order, and target is something that we're looking for
# # Return -1 if not found


# # naive search: scan entire list and ask if its equal to the target
# # if yes, return the index
# # if no, then return -1
# def naive_search(l, target):
#     # example l = [1, 3, 10, 12]
#     for i in range(len(l)):
#         if l[i] == target:
#             return i
#     return -1


# # binary search uses divide and conquer!
# # we will leverage the fact that our list is SORTED
# def binary_search(l, target, low=None, high=None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(l) - 1

#     if high < low:
#         return -1

#     # example l = [1, 3, 5, 10, 12]  # should return 3
#     midpoint = (low + high) // 2  # 2

#     # we'll check if l[midpoint] == target, and if not, we can find out if
#     # target will be to the left or right of midpoint
#     # we know everything to the left of midpoint is smaller than the midpoint
#     # and everything to the right is larger
#     if l[midpoint] == target:
#         return midpoint
#     elif target < l[midpoint]:
#         return binary_search(l, target, low, midpoint-1)
#     else:
#         # target > l[midpoint]
#         return binary_search(l, target, midpoint+1, high)

# if __name__=='__main__':
#     # l = [1, 3, 5, 10, 12]
#     # target = 7
#     # print(naive_search(l, target))
#     # print(binary_search(l, target))

#     length = 10000
#     # build a sorted list of length 10000
#     sorted_list = set()
#     while len(sorted_list) < length:
#         sorted_list.add(random.randint(-3*length, 3*length))
#     sorted_list = sorted(list(sorted_list))

#     start = time.time()
#     for target in sorted_list:
#         naive_search(sorted_list, target)
#     end = time.time()
#     print("Naive search time: ", (end - start), "seconds")

#     start = time.time()
#     for target in sorted_list:
#         binary_search(sorted_list, target)
#     end = time.time()
#     print("Binary search time: ", (end - start), "seconds")

# *****************************************************************************************************************

# [1,2,3,4,5,6,7,8,9,10]
def minmaxGasDist(stations, k):
    # Define a helper function to check if it is possible to achieve a maximum distance
    # between adjacent gas stations less than or equal to the given value (mid).
    def possible(mid):
        count = 0
        for i in range(len(stations) - 1):
            # Calculate the number of additional stations needed to achieve a maximum
            # distance between adjacent stations less than or equal to mid.
            count += int((stations[i + 1] - stations[i]) / mid)
        return count <= k

    # Set the left and right boundaries for binary search.
    left = 0.0
    right = stations[-1] - stations[0]

    # Perform binary search until the left and right boundaries are close enough.
    while right - left > 1e-6:
        mid = (left + right) / 2
        if possible(mid):
            # If it is possible to achieve the desired maximum distance, move the left
            # boundary closer to the right.
            right = mid
        else:
            # If it is not possible, move the right boundary closer to the left.
            left = mid

    return left

print(minmaxGasDist([1,2,3,4,5,6,7,8,9,10], 9))
























    # 