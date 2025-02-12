# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_dict = {value:index for index, value in enumerate(arr2)}
        def customSort(item):
            return (arr2_dict.get(item, len(arr2)), item)
        
        arr1.sort(key=customSort)
    
        return arr1
           
                