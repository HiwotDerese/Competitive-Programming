class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = 0
        visited = set()
        visited.add(0)
        queue = deque([0])

        while queue:
            curr_level = len(queue)
            room = queue.popleft()
            count += 1

            for j in range(len(rooms[room])):
                if rooms[room][j] not in visited:
                    visited.add(rooms[room][j])
                    queue.append(rooms[room][j])

        if count == len(rooms):
            return True

        return False