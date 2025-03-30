# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []
        def helper(curr, path):
            if not curr:
                return
            path.append(curr.val)
            if not curr.left and not curr.right:
                paths.append("".join(map(str, path)))
            else:
                helper(curr.left, path)
                helper(curr.right, path)
            path.pop()
            return paths
        res = helper(root, [])
        summ = 0
        for i in range(len(res)):
            summ += int(res[i])
        return summ


       
            