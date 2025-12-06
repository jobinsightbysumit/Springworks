def immediateBigOnRight(nums1, nums2):
    next_greater = {}
    stack = []

    # Build next greater element map for nums2
    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    # Remaining elements have no next greater
    while stack:
        next_greater[stack.pop()] = -1

    # Build answer for nums1 using the map
    ans = []
    for x in nums1:
        ans.append(next_greater[x])
    return ans
# Example usage:
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(immediateBigOnRight(nums1, nums2))  # Output: [-1, 3, -1]
"""Given two lists of integers, nums1 and nums2, where nums1 is a subset of nums2,
   return a list of the next greater element for each element in nums1
   based on their positions in nums2. If no greater element exists, return -1."""