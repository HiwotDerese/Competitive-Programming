word1 = input()
word2 = input()

word1 = word1[::-1]
word2 = word2[::-1]

# print(word2, word1)

idx, n = 0, min(len(word1), len(word2))

while idx < n and word1[idx] == word2[idx]:
    idx += 1

ans = len(word1[idx:]) + len(word2[idx:])

print(ans)