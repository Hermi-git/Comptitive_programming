# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
                
            left_half = nums[:len(nums)//2]
            right_half = nums[len(nums)//2:]

            left = mergeSort(left_half)
            right = mergeSort(right_half)

            merged = merge(left, right)
            return merged
        def merge(left_half, right_half):
            merged_sort = []
            l = r =0
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    merged_sort.append(left_half[l])
                    l += 1
                else:
                    merged_sort.append(right_half[r])
                    r += 1
            while l < len(left_half):
                merged_sort.append(left_half[l])
                l += 1
            while r<len(right_half):
                merged_sort.append(right_half[r])
                r += 1
            return merged_sort
        return mergeSort(nums)


