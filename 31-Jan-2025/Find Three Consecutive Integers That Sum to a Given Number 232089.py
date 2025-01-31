# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 != 0:
            return []
        num1 = (num - 3)//3
        return [num1, num1+1, num1+2]