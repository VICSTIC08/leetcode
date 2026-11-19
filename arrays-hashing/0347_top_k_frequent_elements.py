"""
347. Top K Frequent Elements | Medium | Arrays & Hashing
Pattern: count with a dict, then bucket sort by count (index = count)
Insight: a count can only be 1..n, so put each number in buckets[count] and read from the top down: no sort needed
Time: O(n), Space: O(n)   (each number lands in exactly one bucket, so the inner loop runs at most n times in total)
Other approaches: sort the unique numbers by count, sorted(counts, key=counts.get, reverse=True)[:k], O(n log n) time / O(n) space; heap of size k, O(n log k) (heaps come later)

Mistakes:
- appended the whole bucket (a list) instead of the numbers inside it, giving nested lists
- reset the result list inside the loop, so it emptied every pass
- counted buckets visited (i) instead of numbers collected; use len(result)
- wrapped the return in [], making a list inside a list
- thought "unique answer" meant counts never tie; counts can tie, so each bucket is a list and needs .append
- Big-O: guessed O(k * (n+1)) for the nested loops; count how many times the inner line runs in total instead (at most n)

Notes:
- sorted(d, key=d.get, reverse=True) sorts the KEYS by their values, biggest first; returns keys only
- lst[:k] = first k items (slicing)
- [[] for _ in range(m)] makes m separate lists; [[]] * m makes m references to ONE list (trap)
- for num, c in d.items() gives (key, value) pairs
- range(start, stop, step): range(len(b) - 1, 0, -1) walks down and stops before 0
- min count is 1 (anything in counts appears at least once), max is n, so n + 1 buckets
- sequential loops add, nested loops multiply, unless the inner loop's total work is bounded (here at most n)
- "unique answer" = only one correct set of k numbers; order doesn't matter
- LeetCode ms / "beats %" is noisy on small inputs; Big-O is what interviews grade
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}  # {number: count}
        for x in nums:
            if x not in counts:
                counts[x] = 1
            else:
                counts[x] += 1

        # index = count (0 stays empty), each bucket = list of numbers with that count
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in counts.items():
            buckets[c].append(num)

        result = []
        for c in range(len(buckets) - 1, 0, -1):  # highest count first
            for num in buckets[c]:
                result.append(num)
                if len(result) == k:
                    return result
        return result  # only reached if k > number of unique values
