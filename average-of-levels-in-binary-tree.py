# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        visited = set([root])
        queue = deque([root])
        ans = []

        while queue:
            curr_level = len(queue)
            level_sum = 0

            for _ in range(curr_level):
                node = queue.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)

                level_sum += node.val 

            level_ave = level_sum / curr_level
            ans.append(level_ave)

        return ans

                





        # visited = set([node])
        # queue = deque([node])

        # while queue:
        #     curr_label = len(queue)
        #     for _ in range(curr_label):
        #         node = queue.popleft()
        #         for neighbour in graph[node]:
        #             if neighbour not in visited:
        #                 queue.append()
        # visited.add(neighbour)
        # queue.append(neighbour)