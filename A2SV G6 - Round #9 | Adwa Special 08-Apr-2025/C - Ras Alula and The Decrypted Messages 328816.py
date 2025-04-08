# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

t = int(input())
for _ in range(t):
    n, m =map(int, input().split())
    decrypt = input()
    sensitive = input()
    sensitive_sum = sum([ord(ch)for ch in sensitive]) 
    decrypt_sum = sum([ord(decrypt[i]) for i in range(m)])
    isPossible = (sensitive_sum == decrypt_sum)
    for i in range(m, n):
        if isPossible:
            break
        decrypt_sum += (ord(decrypt[i]) - ord(decrypt[i-m]))
        if sensitive_sum == decrypt_sum:
            isPossible = True       
    if isPossible:
        print("YES")
    else:
        print("NO")
    
   

   
   