class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #combine the arrays
        combined = nums1 + nums2

        #Sort the combined array
        combined.sort()

        #find the length of the combined array
        length = len(combined)

        #If the length is odd, return the middle element
        if length % 2 == 1:
            return float(combined[length // 2])
        #If the length is even, return the average of the two middle elements
        else:
            mid1 = combined[(length // 2) - 1]
            mid2 = combined[(length // 2)]
            return (float(mid1) + float(mid2)) / 2.0
