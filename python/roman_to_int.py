#Takes 20ms and beats 92.83% of solutions as of 8/5/2024
class Solution(object):
    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary of Roman numerals
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        prev_value = 0

        for char in s[::-1]:  # Iterate from right to left
            current_value = roman_values[char]

            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total

# Create an instance of the Solution class
solution = Solution()

test_cases = [
    "III",      # 3
    "LVIII",    # 58
    "MCMXCIV",  # 1994
    "IV",       # 4
    "IX",       # 9
    "XL",       # 40
    "XC",       # 90
    "CD",       # 400
    "CM",       # 900
]

for roman in test_cases:
    print("{0} = {1}".format(roman, solution.roman_to_int(roman)))
