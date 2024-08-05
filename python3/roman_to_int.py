#Takes 46ms and beats 60% of user solutions
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value

        return total

# Create an instance of the Solution class
solution = Solution()

test_cases = [
    "III",
    "LVIII",
    "MCMXCIV",
    "IV",
    "IX",
    "XL",
    "XC",
    "CD",
    "CM",
]

for roman in test_cases:
    print(f"{roman} = {solution.romanToInt(roman)}")
