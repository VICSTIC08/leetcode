"""
49. Group Anagrams | Medium | Arrays & Hashing
Pattern: group by key, dict {key: [list of items]}
Insight: anagrams sort to the same string, so "".join(sorted(word)) is the group's key
Time: O(n · k log k), Space: O(n · k)   (n words, k = max word length; sorting each word costs k log k)
Other approaches: compare every pair with Valid Anagram, O(n² · k); key = tuple of 26 letter counts, O(n · k)

Mistakes:
- first thought the value should be a count; the output needs the actual words, so the value is a list

Notes:
- a key has one value, but that value can be a list holding many items
- sorted("eat") gives a list ['a','e','t'], which can't be a key; "".join(...) turns it into "aet"
- dicts can't be keys (unhashable); strings and tuples can
- start-or-add pattern: not in d → d[k] = [item], else d[k].append(item)
- d.values() / d.keys() / d.items() → values / keys / (key, value) pairs; wrap in list() to return
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}  # {sorted letters: list of words}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:  # start a new group
                groups[key] = [s]
            else:  # group exists, add to it
                groups[key].append(s)
        return list(groups.values())
