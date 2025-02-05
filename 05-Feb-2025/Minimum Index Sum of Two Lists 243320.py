# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lists_dict = {}
        result = []
        for i in range(len(list1)):
            if list1[i] in list2:
                lists_dict[list1[i]] = i
                lists_dict[list1[i]] += list2.index(list1[i])
        min_index = min(lists_dict.values())
        for value, index in lists_dict.items():
            if index == min_index:
                result.append(value)
        return result