# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0 
        def helper(curr):
            nonlocal count
            if not curr:
                return (0, 0)
            if not curr.left and not curr.right:
                count += 1
                return (curr.val, 1)
            
            left_sum, left_count = helper(curr.left)
            right_sum, right_count = helper(curr.right)

            ave = (left_sum + right_sum + curr.val)// (left_count+right_count +1)

            if ave == curr.val:
                count += 1
            return (left_sum + right_sum + curr.val, left_count+right_count +1)

        helper(root)
        return count
            
