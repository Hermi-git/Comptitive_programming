# Problem: Compare Version Numbers - https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = 0, 0
        ver1= version1.split(".")
        ver2= version2.split(".")
        min_len= min(len(ver1), len(ver2))
        while len(ver1) < len(ver2):
            ver1.append("0")
        while len(ver2) < len(ver1):
            ver2.append("0")
    
        while v1 < len(ver1) and v2<len(ver2):
            if int(ver1[v1]) < int(ver2[v2]):
                return -1
            elif int(ver1[v1]) > int(ver2[v2]):
                return 1
            v1 +=1
            v2 += 1

        return 0
            
            