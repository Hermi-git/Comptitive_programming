# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n, k = map(int, input().split())
A= list(map(int, input().split()))
decrease = deque()
increase = deque()

l = 0
count = 0
for i in range(n):
    while decrease and decrease[-1] < A[i]:
        decrease.pop()
    decrease.append(A[i])
    while increase and increase[-1] > A[i]:
        increase.pop()
    increase.append(A[i])

    while decrease[0] - increase[0] > k:
        val = A[l]
        if decrease[0] == val:
            decrease.popleft()
        if increase[0] == val:
            increase.popleft()
        l+=1
    count += (i-l+1)
print(count)
