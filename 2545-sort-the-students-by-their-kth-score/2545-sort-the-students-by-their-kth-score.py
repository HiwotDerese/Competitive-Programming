class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
         # def sortTheStudents(self, A, k):
        return sorted(score, key=lambda a: -a[k])