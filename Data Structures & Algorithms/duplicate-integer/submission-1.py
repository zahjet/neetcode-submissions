class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isSeen = set()
        for num in nums:
            if num in isSeen:
                return True
            else:
                isSeen.add(num)
        return False