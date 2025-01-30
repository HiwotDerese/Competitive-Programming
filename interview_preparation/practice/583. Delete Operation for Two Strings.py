'''
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2

  
    ''  s   e   a
''  0   1   2   3

e   1   2   1   2

a   2   3   2   1

t   3   4   3   2
'''

def minimumStepsToMakeWordsTheSame(word1, word2):
    n, m = len(word1), len(word2)

    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    print(dp)
    for i in range(n + 1):
        dp[0][i] = i
    print(dp, 'after n')
    for i in range(m + 1):
        dp[i][0] = i

    print(dp, 'before dp')
    for i in range(n):
        for j in range(m):
            if word1[i] == word2[j]:
                dp[i + 1][j + 1] = dp[i][j]

            else:
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + 1
    print(dp)


    return dp[n][m]

print(minimumStepsToMakeWordsTheSame('abc', 'cba'))































   