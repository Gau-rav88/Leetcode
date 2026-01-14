class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)

        return False
        