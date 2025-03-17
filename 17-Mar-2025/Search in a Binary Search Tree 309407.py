# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search_node(curr):
            if not curr:
                return None
            if curr.val == val:
                return curr
            if val < curr.val:
                return search_node(curr.left)
            if val > curr.val:
                return search_node(curr.right)
        return search_node(root)
       