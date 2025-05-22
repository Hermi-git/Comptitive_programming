# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            for key in rooms[node]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        count = 0
        for i in range(len(rooms)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        if count > 1:
            return False
        else:
            return True 
        
