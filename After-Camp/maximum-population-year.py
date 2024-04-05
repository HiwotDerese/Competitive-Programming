class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dic_, n, max_ = defaultdict(int), len(logs), (0, float('inf'))

        for i in range(n):
            start, end = logs[i][0], logs[i][1]

            for j in range(start, end):
                dic_[j] += 1

                if dic_[j] > max_[0] or (dic_[j] == max_[0] and j < max_[1]):
                    max_ = (dic_[j], j)

        return max_[1]