'''
Input: Two arrays, a1 and a2.
Output: An array containing numbers that appear in both a1 and a2, including duplicates, in the order they appear in the first array (a1).
'''


from collections import Counter

def intersect_arrays(a1, a2):
    count_a2 = Counter(a2)
    result = []
    
    for num in a1:
        print(num)
        print('count num', count_a2[num])
        if count_a2[num] > 0:  
            result.append(num)
            count_a2[num] -= 1  
    
    return result

a1 = [1, 5, 2, 3, 4]
a2 = [1, 2, 2]
print(intersect_arrays(a1, a2))  #[1, 2, 2]