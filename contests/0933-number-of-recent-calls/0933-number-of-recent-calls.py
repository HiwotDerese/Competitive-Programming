class RecentCounter:

    def __init__(self):
        self.request = []
        self.left = 0
        

    def ping(self, t: int) -> int:
        _range = [t - 3000, t]
        self.request.append(t)

        if self.request[self.left] >= _range[0]:
            return len(self.request) - self.left

        while self.request[self.left] < _range[0]:
            self.left += 1

        return len(self.request) - self.left
                
            
        
        
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)