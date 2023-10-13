class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        ans = []  
        pq = []

        for x in nums1:
            # print(x, nums2[0])
            heapq.heappush(pq, [x + nums2[0], 0])

        # print(pq, "start")

        while k > 0 and pq:
            pair = heapq.heappop(pq)
            s, idx = pair[0], pair[1]
            # print(pair,s, idx,  "pair")
            ans.append([s - nums2[idx], nums2[idx]]) 

            if idx + 1 < len(nums2):
                heapq.heappush(pq, [s - nums2[idx] + nums2[idx + 1], idx + 1])

            k -= 1
            # print(pq)

        return ans