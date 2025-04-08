# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = None

        def validate(x):
            sub_count = 1
            summ = 0
            for num in nums:
                summ += num
                if summ > x:
                    sub_count += 1
                    summ = num
            return sub_count <= k              
        while low <= high:
            mid = (low+high)//2
            if validate(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans




