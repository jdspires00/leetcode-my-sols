#Solution takes 19ms and beats 99.15% of submisions as of 8/5/2024
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index  = {}
        start = 0
        max_length = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            else:
                max_length = max(max_length, end - start + 1)

            char_index[char] = end

        return max_length
