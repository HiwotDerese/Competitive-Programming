# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bfs(self, node, graph, k):
        visited = set([node])
        queue = deque([node])
        level, ans = 0, []

        while queue:
            curr_level = len(queue)
            if level == k:
                for _ in range(curr_level):
                    ans.append(queue.pop())
                    print(ans)
            
            else:
                for _ in range(curr_level):
                    num = queue.popleft()
                    for i in graph[num]:
                        if i not in visited:
                            visited.add(i)
                            queue.append(i)

                level += 1

        return ans

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root.left and not root.right:
            return []

        graph = defaultdict(list)

        def adj(root):

            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                adj(root.left)

            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                adj(root.right)

        adj(root)

        return self.bfs(target.val, graph, k)