# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        forward = [1] * len(arr)
        backward = [1] * len(arr)
        forward_stack = []
        backward_stack = []
        answer = []
        for i in range(len(arr)):
            while forward_stack and forward_stack[-1][0] >= arr[i]:
                val = forward_stack.pop()
                forward[i] += forward[val[1]]
            forward_stack.append((arr[i], i))
        for j in range(len(arr)-1, -1, -1):
            while backward_stack and backward_stack[-1][0] > arr[j]:
                val = backward_stack.pop()
                backward[j] += backward[val[1]]
            backward_stack.append((arr[j], j))
        for k in range(len(arr)):
            res = forward[k] * backward[k] * arr[k]
            answer.append(res)
        return sum(answer) %(10**9+7)
