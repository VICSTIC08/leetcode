"""
242. Valid Anagram | Easy | Arrays & Hashing
Pattern: counting with a dict {letter: count}
Insight: anagrams = same letters with the same counts; count both strings, compare the dicts
Time: O(n), Space: O(1)   (only 26 lowercase letters, so each dict is capped at 26 keys)
Other approaches: sort both and compare, O(n log n) time / O(n) space; for each letter, search t and cross it out, O(n²)

Mistakes:
- looped with range(len(s)), which gives indices 0, 1, 2, not letters
- checked `x not in s` (the string) instead of the dict
- used one shared count variable; each letter needs its own count, stored in the dict

Notes:
- counting pattern: if ch not in d → d[ch] = 1, else d[ch] += 1
- `for x in thing` gives what's inside it; use range() only when you need indices
- check len(s) != len(t) first for a quick False
- two dicts compare equal with == if they have the same keys and values
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s = {}
        for x in s:
            if x not in seen_s:
                seen_s[x] = 1
            else:
                seen_s[x] += 1

        seen_t = {}
        for x in t:
            if x not in seen_t:
                seen_t[x] = 1
            else:
                seen_t[x] += 1
        return seen_s == seen_t
