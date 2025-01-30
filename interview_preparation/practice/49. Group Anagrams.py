'''
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
aet
aet
{}

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


# Input: strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)

    for str in strs:
        sorted_str = "".join(sorted(str))
        anagrams[sorted_str].append(str)

    ans = []

    for anagram in anagrams:
        ans.append(anagrams[anagram])

    return ans


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]


















