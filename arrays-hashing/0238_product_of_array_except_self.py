"""
238. Product of Array Except Self | Medium | Arrays & Hashing
Pattern: prefix and suffix products (left pass, right pass)
Insight: answer[i] = (product of everything left of i) x (product of everything right of i); build each side in one pass
Time: O(n), Space: O(n)   (three sequential loops add up to 3n; left and right lists hold n each)
Other approaches: brute force, multiply everything except i for each i, O(n^2);
                  total product / nums[i], O(n) but division is banned and it crashes on 0;
                  O(1) extra space follow-up: store left products straight in the answer, then sweep right with a
                  running product s (see the follow-up below)

Mistakes:
- first wrote the division version: banned by the problem, crashes when nums has a 0, and / gives floats
- tried to compute left and right in one loop; going left to right you haven't seen the right side yet,
  so it needs separate passes
- unsure whether the loops nest: they run one after another (sequential = add, not multiply)

Notes:
- left[i] = left[i-1] * nums[i-1]    (product to my left = neighbour's left product x neighbour)
- right[i] = right[i+1] * nums[i+1]  (mirror image)
- start both at 1: the "empty product" (nothing to multiply) is 1, like an empty sum is 0
- [1] * n is safe for numbers; only [[]] * n is the shared-list trap
- range(n - 2, -1, -1) walks backwards and stops BEFORE -1, so index 0 is included
- follow-up trick: ans[i] = p BEFORE p *= nums[i]; storing first leaves "self" out
  (same order as Two Sum's check-before-store)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [1] * len(nums)  # left[i] = product of everything left of i
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]

        right = [1] * len(nums)  # right[i] = product of everything right of i
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        return result


class SolutionO1Space:
    """Follow-up: O(1) extra space (the output list doesn't count)."""

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        p = 1  # product of everything passed so far, going right
        for i in range(n):
            ans[i] = p
            p *= nums[i]
        s = 1  # product of everything passed so far, going left
        for i in range(n - 1, -1, -1):
            ans[i] *= s
            s *= nums[i]
        return ans
