# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

t = int(input())
for _ in range(t):
    n = int(input())
    belts= input()
    if '<' not in belts or '>' not in belts:
        print(n)
    elif '>' in belts and '<' in belts and '-' not in belts:
        print(0)
    else:
        count = 0
        for i in range(n):
            if belts[i] == '-' or belts[(i+1) % n] == '-':
                count += 1
        print(count)

   