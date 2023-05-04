class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n, ans = len(words), []
        dic = Counter(words)
        cnt = []
        for word in dic:
            cnt.append((-dic[word], word))

        heapq.heapify(cnt)

        for i in range(k):
            ans.append(heapq.heappop(cnt)[1])

        return ans