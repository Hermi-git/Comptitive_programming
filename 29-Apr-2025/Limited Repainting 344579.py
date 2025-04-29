# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    paint, block = 1, 2
    penalties = list(map(int, input().split()))
    l, r = 0, max(penalties)
    ans = r

    def feasible(X):
        ops = 0
        in_block = False
        for ci, ai in zip(s, penalties):
            if ai > X and ci == 'R':
                in_block = False
            elif ai > X and ci == 'B':
                if not in_block:
                    ops += 1
                    in_block = True
        return ops <= k

    while l <= r:
        mid = (l + r) // 2
        if feasible(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    print(ans)
