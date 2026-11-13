"""
1. Two Sum | Easy | Arrays & Hashing
Pattern: hash map, "have I seen the partner already?"
Insight: store {number: index}; for each x, look up target - x
Time O(n), Space O(n)   (brute force: O(n²) time, O(1) space)

Mistake: 
- used {x, i} (a set) instead of a dict {key: value}
- wrote seen = {x:i}, which replaces the dict; use seen[x] = i (dict[key] = value) to add 

Notes:
- check before storing in seen, as otherwise x can pair with itself (duplicate index)
- duplicate values are fine
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # {number : index}
        for i, x in enumerate(nums): # grabs i -> x at once
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i