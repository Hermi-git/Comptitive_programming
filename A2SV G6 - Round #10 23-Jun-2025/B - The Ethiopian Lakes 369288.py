# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B


import sys
import threading

input_fn = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
        directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def inbound(row, col):
            return 0<=row<n and 0<=col<m
        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            volume = grid[row][col]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if (inbound(new_row, new_col) and
                    (new_row, new_col) not in visited and
                    grid[new_row][new_col] > 0):
                    volume += dfs(new_row, new_col)
            return volume
    
        max_depth = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and (i, j) not in visited:
                    lake_volume = dfs(i, j)
                    max_depth = max(max_depth, lake_volume)

        
        print(max_depth)

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)


    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
