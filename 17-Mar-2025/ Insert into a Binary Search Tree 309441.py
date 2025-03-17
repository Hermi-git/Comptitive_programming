# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert_node(curr, data):
            if not curr:
                return TreeNode(val)
            if data < curr.val:
                curr.left = insert_node(curr.left, data)
            if data > curr.val:
                curr.right = insert_node(curr.right, data)
            return curr
        return insert_node(root, val)
                