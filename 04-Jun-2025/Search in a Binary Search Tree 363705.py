# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:  # val > curr.val
                curr = curr.right
        return None
       