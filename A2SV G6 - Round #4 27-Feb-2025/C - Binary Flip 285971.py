# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    a += "0"
    b += "0"
    count =0
    for i in range(n):
        if a[i] == "1":
            count += 1
        else:
            count -= 1

        if count != 0:
            if a[i] == b[i] and a[i+1] != b[i+1]:
                print("NO")
                break
            elif a[i] != b[i] and a[i+1] == b[i+1]:
                print("NO")
                break
    else:
        print("YES")
        
            


    