# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        def find_first(l, r):
            nonlocal first
            while l<=r:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                else: 
                    if nums[mid] == target:
                        first = mid
                    r = mid-1
            return first
        def find_last(l,r):
            nonlocal last
            while l <= r:
                mid = (l+r)//2
                if nums[mid] > target:
                    r = mid-1
                else:
                    if nums[mid] == target:
                        last = mid
                    l = mid+1
            return last
        first_pos, last_pos = find_first(0, len(nums)-1), find_last(0, len(nums)-1)
        return [first_pos, last_pos]


        

                    

        
