# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        temp = []
        result = []
        for i in nums_count:
            temp.append([i, nums_count[i]])
        temp.sort(key = lambda temp: temp[1], reverse = True)
        for i in range(k):
            result.append(temp[i][0])
        return result
        


        
        
       
        
            
