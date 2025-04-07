# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        great_sum = 0

        def helper(curr):
            nonlocal great_sum
            if not curr:
                return
            helper(curr.right)
            temp = curr.val
            curr.val += great_sum
            great_sum += temp
            helper(curr.left)
        helper(root)
        return root 
      
