# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        joined_digit = "".join(map(str, digits))
        number = int(joined_digit)
        number = number + 1
        str_num = str(number)
        result = [int(num) for num in str_num]

        return result