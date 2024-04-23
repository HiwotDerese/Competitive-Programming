def largestMerge(word1: str, word2: str):
    len1 = len(word1)
    len2 = len(word2)
    merge = ""
    i = 0
    j = 0
    
    while i < len1 and j < len2:
        if word1[i:] > word2[j:]:
            merge += word1[i]
            i += 1
        else:
            merge += word2[j]
            j += 1
            
    merge += word1[i:] + word2[j:]
    
    return merge

print(largestMerge("guguuuuuuuuuuuuuuguguuuuguug","gguggggggguuggguugggggg"))