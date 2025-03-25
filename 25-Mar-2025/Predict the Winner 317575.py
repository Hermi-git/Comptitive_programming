# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        p1, p2 = 1, 2
        def optimal_game(player, nums):
            if len(nums) == 1:
                if player == p1:
                    return nums[0], 0
                if player == p2:
                    return 0, nums[0]
            if player == p1:
                selected_first = optimal_game(p2, nums[1:])
                selected_last = optimal_game(p2, nums[:-1])
                if selected_first[0] + nums[0] > selected_last[0] + nums[-1]:
                    return selected_first[0] + nums[0], selected_first[1]
                else:
                    return selected_last[0] + nums[-1], selected_last[1]
            if player == p2:
                selected_first = optimal_game(p1, nums[1:])
                selected_last = optimal_game(p1, nums[:-1])
                if selected_first[1] + nums[0] > selected_last[1] + nums[-1]:
                    return selected_first[0], selected_first[1] + nums[0]
                else:
                    return selected_last[0], selected_last[1] + nums[-1]
        p1_score, p2_score = optimal_game(p1, nums)
        return p1_score >= p2_score
