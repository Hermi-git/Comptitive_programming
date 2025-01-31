# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
compare_str = "codeforces"
for _ in range(t):
    s = input()
    p1, p2 = 0, 0
    differ_indicies = 0
    while p1 < 10 and p2 < 10:
        if s[p1] != compare_str[p2]:
            differ_indicies += 1
        p1 += 1
        p2 += 1
    print(differ_indicies)