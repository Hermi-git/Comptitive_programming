# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert_string(bits):
            return "".join("1" if bit == "0" else "0" for bit in bits)
        def reverse_string(bits):
           return bits[::-1]
        def concatination(n):
            if n == 1:
                return "0"
            return concatination(n-1) + "1" + reverse_string(invert_string(concatination(n-1)))
       
        binary = concatination(n)
        return binary[k-1]
        