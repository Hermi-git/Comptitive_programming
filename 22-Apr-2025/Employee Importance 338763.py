# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id:emp for emp in employees}
        def dfs(emp):
            importance = emp_map[emp].importance
            for sub in emp_map[emp].subordinates:
                importance += dfs(sub)
            return importance
        return dfs(id) 
          