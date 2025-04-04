# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def level_order(curr, level=1):
            if not curr:
                return
            result.append((level, curr.val))
            if curr.left:
                level_order(curr.left, level+1)
            if curr.right:
                level_order(curr.right, level+1)
        level_order(root)
        dictt = defaultdict(list)
        for level, val in result:
            dictt[level].append(val)
        ans = []
        for key in dictt:
            if key % 2 == 0:
                n = len(dictt[key])
                ans.append(dictt[key][::-1])
            else:
                ans.append(dictt[key])
        return ans
            
