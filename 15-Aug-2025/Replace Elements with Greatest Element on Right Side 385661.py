# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_sofar = -1
        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = max_sofar
            max_sofar = max(max_sofar, curr)
        return arr