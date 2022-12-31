tests = int(input())

for i in range(tests):
    word = input().split()
    answer = []

    for wrd in word:

        word2 = ""
        idx = 0
        ans = []
        for i in range(len(wrd)):

            if wrd[i].isdigit():
                idx = (idx * 10) + int(wrd[i])
            else:
                word2 += wrd[i]
        answer.append((idx,word2))
    answer.sort()
    for i in range(len(answer)):
        ans.append(answer[i][1])

    print(" ".join(ans))

