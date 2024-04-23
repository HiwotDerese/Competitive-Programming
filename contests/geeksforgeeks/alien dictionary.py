#User function Template for python3
from collections import defaultdict, deque


class Solution:
    
    def toposort(self, graph, k):
        in_degree = {v: 0 for v in range(k)}
        
        for v in graph:
            for neighbor in graph[v]:
                in_degree[neighbor] += 1
    
        queue = deque([v for v in in_degree if in_degree[v] == 0])
        result = []
        
        while queue:
            v = queue.popleft()
            result.append(v)
            
            for neighbor in graph[v]:
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result
            
        
    def findOrder(self,alien_dict, N, K):
        graph =defaultdict(list)

        for i in range(N - 1):
            m = min(len(alien_dict[i + 1]), len(alien_dict[i]))
            
            for j in range(m):
                if (alien_dict[i][j] != alien_dict[i + 1][j]):
                    graph[ord(alien_dict[i][j]) - ord('a')].append(ord(alien_dict[i + 1][j]) - ord('a'))
                    
                    break

        topo_sorted = self.toposort(graph, k)
        ans = ""
        
        for char in topo_sorted:
            ans += chr(char + ord('a'))
            
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends