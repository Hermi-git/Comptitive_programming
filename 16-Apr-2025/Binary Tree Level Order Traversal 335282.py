# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        level = 0
        ans = []
        cur_level_elem = []
        
        while queue:
            node, nodelevel = queue.popleft()

            if not node:
                continue
            if level != nodelevel:
                ans.append(cur_level_elem[:])
                level += 1
                cur_level_elem = []
            cur_level_elem.append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        if cur_level_elem:
            ans.append(cur_level_elem[:])
        return ans 
