# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    def greater(nums):
        prefix = [0,nums[0]]
        stack = []
        for i in range(1, n):
            prefix.append(prefix[-1]+nums[i])
        
    
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] <= num:
                idx = stack.pop()

                if prefix[i] - prefix[idx] > 0:
                    return False
            stack.append(i)
        return True
    
    if greater(nums) and greater(nums[::-1]):
        print("YES")
    else:
        print("NO")


    