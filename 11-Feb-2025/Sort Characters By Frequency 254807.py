# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count_str = Counter(s)
        def customSort(item):
            return (count_str[item], item)
        
        sorted_s = sorted(s, key = customSort, reverse = True)
        return "".join(sorted_s)