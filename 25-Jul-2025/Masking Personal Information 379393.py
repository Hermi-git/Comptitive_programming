# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            s = s.lower()
            name, domain = s.split("@")
            s = name[0] + "*****" + name[len(name)-1] + "@" + domain
        else:
            cnt = 0
            digits = ""
            for digit in s:
                if digit.isdigit():
                    cnt += 1
                    digits += digit
            
            if cnt == 10:
                s = "***-***-" +  digits[-4:]
            elif cnt == 11:
                s = "+*-***-***-" + digits[-4:]
            elif cnt == 12:
                s = "+**-***-***-" + digits[-4:]
            elif cnt == 13:
                s = "+***-***-***-" + digits[-4:]
        
        return s


                

      

            

            
            