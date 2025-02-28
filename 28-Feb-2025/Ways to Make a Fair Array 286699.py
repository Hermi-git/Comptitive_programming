# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_prefix = [0] * (n+1)
        odd_prefix = [0] * (n+1)

        for i in range(n):
            even_prefix[i+1] = even_prefix[i] + (nums[i] if i % 2 == 0 else 0)
            odd_prefix[i+1] = odd_prefix[i] + (nums[i] if i % 2 == 1 else 0)
        
        res =0
        for j in range(1, n+1):
            odd_left = odd_prefix[j-1]
            even_left = even_prefix[j-1]

            odd_right = even_prefix[-1] - even_prefix[j]
            even_right = odd_prefix[-1] - odd_prefix[j]

            if odd_left + odd_right == even_left + even_right:
                res += 1
        return res


        