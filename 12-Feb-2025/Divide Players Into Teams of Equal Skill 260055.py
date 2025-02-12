# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        valid_team = set()
        while left < right:
            valid_team.add(skill[left] + skill[right])
            left += 1
            right -= 1
        res = 0
        l, r = 0, len(skill)-1
        if len(valid_team) == 1:  
            while l < r:
                chemistry = skill[l] * skill[r]
                res += chemistry
                l += 1
                r -= 1
        return res if res else -1
            