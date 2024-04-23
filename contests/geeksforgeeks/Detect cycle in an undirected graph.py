from typing import List
class Solution:
    
    def hascycle(self, node, parent, adj, visited):
        
        visited.add(node)
            
        
        for neighbor in adj[node]:
            if neighbor not in visited:
                if self.hascycle(neighbor, node, adj, visited):
                    return True
                
            elif neighbor != parent:
                return True
                
        return False
                
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		
		for i in range(v):
		    if i not in visited:
		        if self.hascycle(i, None, adj, visited):
		            return 1
		            
		return 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends