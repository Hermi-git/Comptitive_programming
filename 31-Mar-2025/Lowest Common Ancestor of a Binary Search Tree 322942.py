# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def helper(curr):
            nonlocal ans
            if p.val <= curr.val <= q.val or q.val <= curr.val<= p.val:
                ans = curr
                return curr
            if p.val > curr.val and q.val>curr.val:
                return helper(curr.right)
            if p.val < curr.val and q.val<curr.val:
                return helper(curr.left)
        helper(root)
        return ans 
        

        
            
