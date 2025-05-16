# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [arr[0]]
        for i in range(1, len(arr)):
            pref.append(pref[i-1]^arr[i])
        answer = [0]*len(queries)
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]
            answer[i] = pref[right] ^ pref[left-1] if  left > 0 else pref[right] 
        return answer