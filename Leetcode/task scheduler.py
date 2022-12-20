class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = Counter(tasks)
        freq = []
        for i in dic:
            freq.append(dic[i])
        max_freq = max(freq)
        max_task = freq.count(max_freq)
        ans = ((max_freq - 1) * (n+1)) + max_task 
        return max(len(tasks),ans)