# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        join_digit = "".join(map(str, digits))
        numb = int(join_digit)
        numb = numb + 1
        str_num = str(numb)
        res = [int(num) for num in str_num]

        return res