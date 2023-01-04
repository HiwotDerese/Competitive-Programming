class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for i in range(len(cpdomains)):
            string = cpdomains[i].split()
            leng = len(string[1].split("."))
            
            for j in range(leng):
                domain = string[1].split(".", j)
                # print(domain)
                
                if domain[j] in dic:
                    # print(string[0])
                    dic[domain[j]] += int(string[0])
                    
                else:
                    dic[domain[j]] = int(string[0])
        # print(dic)
        # return dic
        ans = []
        # print(len(dic))
        for i in dic:
            stri = ""
            stri += str(dic[i]) + " " + str(i)
            ans.append(stri)
        return ans
            
            
                
                
            
            
        