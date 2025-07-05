# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)

        maximum = 1
        l = 0
        
        for r in range(1, len(arr)):
            
            if arr[r] == arr[r - 1]:
                l = r
            elif r == 1 or (arr[r] > arr[r - 1] and arr[r - 1] <= arr[r - 2]) or (arr[r] < arr[r - 1] and arr[r - 1] >= arr[r - 2]):
                maximum = max(maximum, r - l + 1)
            else:
                l = r - 1
        
        return maximum

            