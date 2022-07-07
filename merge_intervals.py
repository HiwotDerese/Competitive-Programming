class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        nonOverlap_list = []
        for i in range(len(intervals) - 1):
            if i == 0:
                if intervals[i][1] > intervals[i + 1][0]:
                    elt = []
                    elt.insert(0,intervals[i][0])
                    elt.insert(1,intervals[i + 1][1])
                    nonOverlap_list.append(elt)
                else:
                    nonOverlap_list.append(intervals[i])
            else:
                if not intervals[i - 1][1] > intervals[i][0]:
                    if nonOverlap_list[-1][1] > intervals[i + 1][0]:
                        elt = []
                        elt.insert(0,nonOverlap_list[i - 1][0])
                        elt.insert(1,intervals[i + 1][1])
                        nonOverlap_list.append(elt)
                    else:
                        nonOverlap_list.append(intervals[i])
        nonOverlap_list.append(intervals[i + 1])
                
        return nonOverlap_list
    
    
    
