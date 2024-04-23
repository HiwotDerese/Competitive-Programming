class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        wheels = [0] * 4
        ans = 0
        queue, way = deque([wheels]), ''.join(map(str, wheels))
        visited = set(way)


        # arr = [0]
        # b = arr
        # b[0] = 4
        # print(arr)

        def getneibours(nums):
            neibours = []

            for i in range(len(nums)):
                arr = nums[::]

                num = nums[i]
                temp = (num + 1) % 10
                hold = arr[i]

                arr[i] = temp
                neibours.append(arr.copy())
                temp = (num - 1) % 10
                arr[i] = temp
                neibours.append(arr.copy())

                arr[i] = hold

            return neibours       

        while queue:
            curr_level = len(queue)

            for i in range(curr_level):
                nums = queue.popleft()
                way = ''.join(map(str, nums))
                if way == target:
                    return ans
                adj = getneibours(nums)
                # print(way, adj)
                # print(adj, visited)
                for path in adj:
                    m = ''.join(map(str, path))
                    if m not in visited and m not in deadends:
                        visited.add(m)
                        queue.append(path)

            ans += 1

        return -1