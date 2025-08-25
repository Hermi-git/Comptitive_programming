# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0] * n

        def find( X):
            if X == parent[X]:
                return parent[X]
            parent[X] =  find(parent[X])
            return parent[X]
        
        def union(X, Y):
            parentX, parentY = find(X), find(Y)
            if parentX != parentY:
                rankX = rank[parentX]
                rankY = rank[parentY]
                if rankX > rankY:
                    parent[parentY] = parentX
                elif rankX < rankY:
                    parent[parentX] = parentY
                else:
                    parent[parentY] = parentX
                    rank[parentX] += 1

        number_of_provinces = n
        for r in range(n):
            for c in range(r+1, n):
                parentC = find(c)
                parentR = find(r)
                if isConnected[r][c] == 1 and parentR != parentC:
                    number_of_provinces -= 1
                    union(r, c)
        
        return number_of_provinces

