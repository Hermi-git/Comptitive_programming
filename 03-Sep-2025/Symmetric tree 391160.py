# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry(item , image):
            if not item and not image:
                return True
            if (item and not image) or( image and not item) :
                return False
            if item.val != image.val:
                return False
            else:
                return symmetry(item.right, image.left) and symmetry(item.left, image.right)
       
        return symmetry(root, root)

        