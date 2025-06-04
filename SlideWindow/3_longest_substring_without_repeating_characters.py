"""
Problem:

Given a string s, find the length of the longest substring without duplicate characters.

Clarify:

Input: s: str

Output: length: int, length of the longest substring without duplicate characters

Questions:

What kind of char contains in s? alphabets, digits, spaces, symbol

Will s empty? Yes

Max length of s? 5 * 10^4

Example dry run:

s = "abcabcbb"

a, ab, abc, abca, abcab....
b, bc, bca, bcab, bcabc...
c, ca, cab, cabc, cabcb
make sure every string has no duplicate char
get max(len(every string))

O(2^n) for Time
O(1) for Space

Observation:

When I make sub string, if it already have duplicate char, I can skip this string

=> Slide Window
O(n) for Time
O(n) for Space

Solutions:

1. Brute force: O(2^n) for Time, O(1) for Space
2. Slide Window: O(n) for Time, O(n) for Space

=> Slide Window

window = set()
left = 0

substring_length = 0

for char in s:
    while char in window:
        window.remove(s[left])
        left += 1
    
    window.add(char)
    substring_length = max(substring_length, len(window))

return substring_length

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        substring_length = 0

        for char in s:
            while char in window:
                window.remove(s[left])
                left += 1

            window.add(char)
            substring_length = max(substring_length, len(window))
        
        return substring_length

"""
s = "pwwkew"

i = 0, window = {p}, left = 0, substring_length = 1
i = 1, window = {p, w}, substring_length = 2
i = 2, window = {w}, left = 2, substring_length = 2
i = 3, window = {w, k}, substring_length = 2
i = 4, window = {w, k, e}, substring_length = 3
i = 5, window = {k, e, w}, substring_length = 3

substring_length = 3

s = ""

substring_length = 0

"""