# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(obj , image):
            if not obj and not image:
                return True
            if (obj and not image) or( image and not obj) :
                return False
            if obj.val != image.val:
                return False
            else:
                return check_symmetry(obj.right, image.left) and check_symmetry(obj.left, image.right)
       
        return check_symmetry(root, root)

        