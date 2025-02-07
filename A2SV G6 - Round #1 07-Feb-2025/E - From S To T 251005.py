# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

q = int(input())
for _ in range(q):
    s = input()
    t = input()
    p = input()
    
    i, j = 0, 0

    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    if i < len(s):  
        print("NO")
        continue  

    
    count_t = {}
    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    
    count_s_p = {}
    for ch in s + p:
        count_s_p[ch] = count_s_p.get(ch, 0) + 1

    for ch, req in count_t.items():
        if count_s_p.get(ch, 0) < req:
            print("NO")
            break  
    else:
        print("YES")  
