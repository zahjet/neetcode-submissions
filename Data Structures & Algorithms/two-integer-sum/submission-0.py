class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,key in enumerate(nums):
            diff = target-key
            if diff in hashmap:
                return [hashmap[diff],index]
            hashmap[key] = index