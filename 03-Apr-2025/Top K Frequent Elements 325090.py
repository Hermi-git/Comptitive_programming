# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        nums_count = Counter(nums)
        maxi = max(nums_count.values())
        buckets = [[]for i in range(maxi+1)]
        for key, value in nums_count.items():
            buckets[value].append(key)
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                if len(result)< k:
                    result.append(buckets[i][j])
        return result

        


        
        
       
        
            
