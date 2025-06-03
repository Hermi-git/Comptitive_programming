# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first] * (len(encoded)+1)
        for i in range(len(encoded)):
            answer[i+1] = encoded[i] ^ answer[i]
        return answer