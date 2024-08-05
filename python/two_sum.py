#Solution is the acceptable answer with time complexity of less than O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target -num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

# Test cases
def run_tests():
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test case 1:")
    print("Input: nums = {0}, target = {1}".format(nums1, target1))
    print("Output: {0}".format(solution.twoSum(nums1, target1)))
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print("\nTest case 2:")
    print("Input: nums = {0}, target = {1}".format(nums2, target2))
    print("Output: {0}".format(solution.twoSum(nums2, target2)))
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("\nTest case 3:")
    print("Input: nums = {0}, target = {1}".format(nums3, target3))
    print("Output: {0}".format(solution.twoSum(nums3, target3)))

# Run the tests
run_tests()
