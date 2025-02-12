# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        k = []

        for i in range(n):
            max_val = max(arr[:n-i]) 
            max_idx = (arr.index(max_val) + 1)
            arr[:max_idx] = reversed(arr[:max_idx])
            k.append(max_idx)
            

            arr[:n-i] = reversed(arr[:n-i])
            k.append(n-i)
        
        return k