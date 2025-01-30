'''
Input Data:

you will get a notifications in the form {user, item, date}.
An operation that queries the top k sold items.
Output:

The top k items sorted by their sales count (and optionally by some secondary criterion, like lexicographical order, if there's a tie).
'''


import heapq
from collections import defaultdict

class AmazonSalesTracker:
    def __init__(self):
        self.sales_count = defaultdict(int)  

    def sell_item(self, item):
        self.sales_count[item] += 1
        print(self.sales_count.items())

    def get_top_k_items(self, k):
        min_heap = []
        for item, count in self.sales_count.items():
            heapq.heappush(min_heap, (count, item))  
            print('min heap orign', min_heap, '*********************************')
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)  

        print(min_heap, 'heap before answer')
        return sorted(min_heap, key=lambda x: (-x[0], x[1]))


tracker = AmazonSalesTracker()

tracker.sell_item("item1")
tracker.sell_item("item1")
tracker.sell_item("item2")
tracker.sell_item("item3")
tracker.sell_item("item2")

top_k_items = tracker.get_top_k_items(2)
print("Top 2 sold items:", [(item, count) for count, item in top_k_items])
