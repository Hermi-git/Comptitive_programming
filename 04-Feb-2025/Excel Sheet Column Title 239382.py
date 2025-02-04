# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter = "" 
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            letter += chr(65 + remainder)
            columnNumber = columnNumber // 26
            
        final_letter = letter[::-1]
        return final_letter