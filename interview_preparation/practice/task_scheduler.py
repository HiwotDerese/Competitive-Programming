"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, 
but there's a constraint:there has to be a gap of at least n intervals between two tasks with the same label.
Return the minimum number of CPU intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6

"""

import heapq
from typing import Counter
from collections import deque


def find_minimum_interval(tasks, n):

    dic = Counter(tasks)
    arr = []
    for i in dic:
        arr.append(dic[i])

    max_heap = [-num for num in arr]
    heapq.heapify(max_heap)

    queue = deque()
    ans = 0
    time = 0
    # print(queue, max_heap)
    while queue or max_heap:
        # print(queue, max_heap)
        if queue and queue[0][1] == time:
            heapq.heappush(max_heap, -queue[0][0])
            queue.popleft()

        ans += 1
        if max_heap:
            time += 1
            max_ = -heapq.heappop(max_heap)
            if max_ - 1:
                queue.append((max_ - 1, time + n))

        # print('time and answer')
        print(time, ans)

    return ans


print(find_minimum_interval(["A", "C", "A", "B", "D", "B", "B"], 1))
print(find_minimum_interval(["A", "A", "A", "B", "B", "B"], 2))
print(find_minimum_interval(["A", "A", "A", "B", "B", "B"], 3))
