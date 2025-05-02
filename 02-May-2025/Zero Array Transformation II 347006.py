# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l, r, ans= 0, len(queries)-1, -1
        if sum(nums) == 0:
            return 0
        def can_zero(ops):
            arr = [0] * (len(nums) +1)
            for i in range(ops+1):
                arr[queries[i][0]] += queries[i][2]
                arr[queries[i][1]+1] -= queries[i][2]
            prefix = [arr[0]]
            for i in range(1, len(arr)):
                prefix.append(prefix[i-1]+arr[i])
            for i in range(len(nums)):
                if prefix[i] < nums[i]:
                    return False
            return True

        while l <= r:
            mid = (l+r)//2
            if can_zero(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        if(ans == -1):
            return ans
        else:
            return ans +1

        
