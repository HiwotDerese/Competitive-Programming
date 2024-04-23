class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        answers = []
        sorted(citations)
        if citations[-1] == 0:
            return 0
        if len(citations) == 1:
            return 1
        for i in range(len(citations)):
            if citations[i] == 0:
                continue
            for j in range(len(citations)):
                if citations[j] >= citations[i]:
                    count += 1
            if count == citations[i]:
                answers.append(citations[i])
        if len(answers) == 1:
            return answers[0]
        elif len(answers) == 0:
            return 1
        else:
            sorted(answers)
            # x = len(answers) - 1
            return answers[-1]
                