"""
217. Contains Duplicate | Easy | Arrays & Hashing
Pattern: hash set, "have I seen this before?"
Insight: only need yes/no (no index to return), so a set is enough; dict only when you need a value attached
Time: O(n), Space: O(n)
Other approaches: brute force O(n²) time / O(1) space; sort first O(n log n) time / O(1) space

Mistakes:
- used a dict storing indices I never used; set does the same job with less

Notes:
- list `in` is O(n); set/dict `in` is O(1)
- seen = set(), not {}: empty braces make a dict
- don't use enumerate if you don't need the index
- early return beats len(set(nums)) != len(nums) when the duplicate is near the start
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False