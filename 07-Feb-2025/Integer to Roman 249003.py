# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        str_num = str(num)
        n = len(str_num)
        intToRoman = {
                1:"I",
                4: "IV",
                9: "IX",
                40:"XL",
                90:"XC",
                400:"CD",
                900:"CM",
                5: "V",
                10: "X",
                50: "L",
                100: "C",
                500: "D",
                1000: "M"
        }
        result = []
        for i in range(n):
            if int(str_num[i]) *(10**(n-1-i)) in intToRoman:
                result.append(intToRoman[int(str_num[i]) *(10**(n-1-i))])

            elif int(str_num[i]) < 4:
                val =  intToRoman[10**(n-1-i)]*int(str_num[i])
                result.append(val)
            elif int(str_num[i])>5:
                value=[]
                value.append(intToRoman[5*(10**(n-1-i))])
                remainder = int(str_num[i]) -5
                value.append(intToRoman[10**(n-1-i)]*remainder)
                result.append("".join(value))
        return "".join(result)
        
                

            


