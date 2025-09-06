# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_join = "".join(map(str, digits))
        numb = int(digits_join)
        numb = numb + 1
        num_str = str(numb)
        ans = [int(num) for num in num_str]

        return ans