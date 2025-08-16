# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt_5 = 0
        cnt_10 = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                cnt_5 += 1
            if bills[i] == 10 :
                cnt_10 += 1
                if cnt_5 < 1:
                    return False
                cnt_5 -= 1
            if bills[i] == 20:
                if cnt_10 >= 1 and cnt_5 >= 1:
                    cnt_10 -= 1
                    cnt_5 -= 1
                elif cnt_5 >= 3 :
                    cnt_5 -= 3
                else:
                    return False
                
        return True
                
                
