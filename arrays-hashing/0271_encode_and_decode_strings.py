"""
271. Encode and Decode Strings | Medium | Arrays & Hashing   (Premium on LeetCode; free on NeetCode)
Pattern: length-prefix encoding, each string becomes len + "#" + string
Insight: separators fail because strings can contain any character; a length tells the decoder exactly
         how many characters to read, so the content never matters. The "#" only marks where the number ends.
Time: O(m) for encode and decode, Space: O(m + n)   (m = total characters, n = number of strings; each character is read once)
Other approaches: join with a separator (breaks on ["a,b", "c"]); escape the separator inside strings (works but fiddly);
                  all lengths at the front (ambiguous once a length has 2+ digits)

Mistakes:
- first tried a separator (#) between strings; a "#" inside a string breaks it
- put all the lengths at the front ("543..."), ambiguous once a length has 2+ digits
- counted len("i, vic") as 5; spaces count, it's 6
- wrote `str s` (C-style declaration); Python has no declarations, just assign
- wrote s[a, b] instead of s[a:b]
- encode: built into an undefined variable, then overwrote the loop variable
- decode: measured the slice from i (start of the number) instead of j (the "#"), then guessed offsets (i+2, j+2)
- wrote i += j + 1 + length instead of i = j + 1 + length

Notes:
- two indices that mean different things: i = start of the number, j = the "#"
  string = s[j+1 : j+1+length], next i = j + 1 + length
- use a while loop with your own index when you need to jump ahead, not step one character at a time
- s[a:b] includes a, excludes b
- += moves BY an amount, = moves TO a position
- int("12") gives 12, str(12) gives "12"
- empty string encodes as "0#" and decodes as s[j+1:j+1] = ""
"""
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # i = start of the length number
        while i < len(s):
            j = i  # j walks to the "#"
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
