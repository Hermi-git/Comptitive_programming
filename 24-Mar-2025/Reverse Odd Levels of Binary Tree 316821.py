# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(curr1, curr2, level=1):
            if not curr1 or not curr2:
                return
            if level % 2 == 1:
                curr1.val, curr2.val = curr2.val, curr1.val
            reverse(curr1.left, curr2.right, level + 1)
            reverse(curr1.right, curr2.left, level + 1)
        
        reverse(root.left, root.right, 1)
        return root

