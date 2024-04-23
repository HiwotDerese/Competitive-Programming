class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        stack = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        arr.sort(reverse = True)
        for i in range(len(position)):
            t = (target - arr[i][0]) / arr[i][1]
            if not stack or t > stack[-1]:
                stack.append(t)
                
        return len(stack)
            
        