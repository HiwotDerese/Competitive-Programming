tests = int(input())

for _ in range(tests):
    num_of_strings = int(input())
    phrases = {}
    words = []

    for _ in range(num_of_strings):
        word = input()
        phrases[word] = False
        words.append(word)

    for word in words:
        word_len = len(word)

        for i in range(word_len):
            partition1 = word[:i+1]
            partition2 = word[i+1:]
            if partition1 in phrases and partition2 in phrases:
                phrases[word] = True
                break

    for word in words:
        value = 1 if phrases[word] else 0
        print(value, end="")
        
    print()


# abab
# a, bab
# ab, ab
# aba, b