# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

import sys
input = sys.stdin.readline

def binary_search(val):
    l, r = 0, m - 1
    ans = None
    while l <= r:
        mid = (l + r) // 2
        if b[mid] >= val:
            ans = b[mid]
            r = mid - 1
        else:
            l = mid + 1
    return ans

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    temp = []
    # initialize temp[0]
    # both options always ≥ -inf, so pick the smaller
    first_keep = a[0]
    first_trans = b[0] - a[0]
    temp.append(min(first_keep, first_trans))

    possible = True
    for i in range(1, n):
        prev = temp[-1]

        # option 1: keep a[i] if it doesn't drop below prev
        keep = a[i] if a[i] >= prev else None

        # option 2: transform using smallest b[j] ≥ (prev + a[i])
        needed = prev + a[i]
        res = binary_search(needed)
        trans = (res - a[i]) if res is not None else None

        # collect only valid choices
        candidates = []
        if keep is not None:
            candidates.append(keep)
        if trans is not None:
            candidates.append(trans)

        if not candidates:
            possible = False
            break

        # pick the smaller to stay as “low” as possible
        temp.append(min(candidates))

    print("YES" if possible else "NO")
