# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    if x == 1:
        print(3)
    elif x % 2 != 0:
        print(1)  
    else:
        low_bit = x & -x
        if x ^ low_bit > 0:
            print(low_bit)
        else:
            print(low_bit + 1)

