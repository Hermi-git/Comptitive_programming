# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def max_depth(curr, level=1):
            if not curr:
                return
            result.append((level, curr.val)) 
            if curr.left:
                max_depth(curr.left, level + 1)
            if curr.right:
                max_depth(curr.right, level + 1)
        max_depth(root)
        dictt = defaultdict(list)  
        for level, val in result:
            dictt[level].append(val)
        answer =[]
        for key in dictt:
            answer.append(max(dictt[key]))
        return answer


    



     