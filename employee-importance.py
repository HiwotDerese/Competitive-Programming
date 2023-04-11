"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def totalImportance(self, employee, ans, employees):
        self.ans += employee.importance

        for i in employee.subordinates:
            # if s:
            #     ans = s[-1]
            for j in range(len(employees)):
                if employees[j].id == i:
                    break

            self.totalImportance(employees[j], self.ans, employees)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.ans = 0
        for i in range(len(employees)):
            if employees[i].id == id:
                break

        self.totalImportance(employees[i], self.ans, employees)
        return self.ans