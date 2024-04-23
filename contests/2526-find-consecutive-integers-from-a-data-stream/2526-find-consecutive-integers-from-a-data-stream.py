class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.size = k
        

    def consec(self, num: int) -> bool:
        if self.size > 0:
            self.size -= 1
            
#         the numbers inserted should be consicuative   
        if num != self.value:
            self.size = self.k
        
        if self.size > 0:
            return False
        
#         if self.size = 0 it means there are k consequetive num == val
        return True
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)