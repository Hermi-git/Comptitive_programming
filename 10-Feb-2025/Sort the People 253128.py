# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            max_idx = i
            for j in range(i+1, n):
                if heights[j] > heights[max_idx]:
                    heights[max_idx], heights[j] = heights[j], heights[max_idx]
                    names[max_idx], names[j] = names[j], names[max_idx]
        return names
            

