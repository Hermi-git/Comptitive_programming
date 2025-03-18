# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
from math import ceil

def input():
    return sys.stdin.readline().strip()

def minimum_kicks(s):
    total_kicks = 10
    confirmed1, confirmed2 = 0, 0
    uncertain1, uncertain2 = 0, 0
    
    for i in range(total_kicks):
        kicks_left = total_kicks - i  
        
        if i % 2 == 0:  
            if (confirmed1 + ceil(kicks_left / 2) < confirmed2 + uncertain2 or
                confirmed2 + (kicks_left // 2) < confirmed1 + uncertain1):
                return i  
            if s[i] == '1':
                confirmed1 += 1
            elif s[i] == '?':
                uncertain1 += 1
                
        else:  
            if (confirmed2 + ceil(kicks_left / 2) < confirmed1 + uncertain1 or
                confirmed1 + (kicks_left // 2) < confirmed2 + uncertain2):
                return i 
            if s[i] == '1':
                confirmed2 += 1
            elif s[i] == '?':
                uncertain2 += 1
                
    return total_kicks  

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(minimum_kicks(s))
