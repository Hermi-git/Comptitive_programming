# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        paths_dict = defaultdict(list)

        for path in paths:
            dire, *files = path.split(" ")

            for file in files:
                fname, fcontent = file.split("(")
                paths_dict[fcontent].append(dire + "/" + fname)
            result = []
            for value in paths_dict.values():
                if len(value) > 1:
                    result.append(value)
        return result
                

            