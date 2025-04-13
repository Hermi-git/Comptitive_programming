# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        def inorder(curr):
            if curr:
                inorder(curr.left)
                result.append(curr.val)
                inorder(curr.right)
        inorder(root)
        def heightBalance(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            root = TreeNode(val = result[mid])
            root.left = heightBalance(l, mid-1)
            root.right = heightBalance(mid+1, r)
            return root
        return heightBalance(0, len(result)-1)
