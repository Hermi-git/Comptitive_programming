# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        t1, t2 = 1, 2
        def optimal_game(player, nums):
            if len(nums) == 1:
                if player == t1:
                    return nums[0], 0
                if player == t2:
                    return 0, nums[0]
            if player == t1:
                selected_first = optimal_game(t2, nums[1:])
                selected_last = optimal_game(t2, nums[:-1])
                if selected_first[0] + nums[0] > selected_last[0] + nums[-1]:
                    return selected_first[0] + nums[0], selected_first[1]
                else:
                    return selected_last[0] + nums[-1], selected_last[1]
            if player == t2:
                selected_first = optimal_game(t1, nums[1:])
                selected_last = optimal_game(t1, nums[:-1])
                if selected_first[1] + nums[0] > selected_last[1] + nums[-1]:
                    return selected_first[0], selected_first[1] + nums[0]
                else:
                    return selected_last[0], selected_last[1] + nums[-1]
        t1_score, t2_score = optimal_game(t1, nums)
        return t1_score >= t2_score
