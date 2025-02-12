# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        result = []

        while score:  
            max_row = max(score, key=lambda row: row[k]) 
            result.append(max_row)  
            score.remove(max_row)  
        
        return result
