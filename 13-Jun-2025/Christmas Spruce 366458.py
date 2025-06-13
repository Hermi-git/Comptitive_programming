# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

nodes = int(input())
trees = [[] for _ in range(nodes+1)]
for child in range(2, nodes+1):
    parent = int(input())
    trees[parent].append(child)

is_spruce = True
for node in range(1, nodes+1):
    if len(trees[node]) == 0:
        continue

    leaf_count = 0
    for child in trees[node]:
        if len(trees[child]) == 0:
            leaf_count += 1
    if leaf_count < 3:
        is_spruce = False
        break

if is_spruce:
    print("Yes")
else:
    print("No")