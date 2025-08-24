# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert_node(current, data):
            if not current:
                return TreeNode(data)
            if data < current.val:
                current.left = insert_node(current.left, data)
            if data > current.val:
                current.right = insert_node(current.right, data)
            return current
        return insert_node(root, val)
                