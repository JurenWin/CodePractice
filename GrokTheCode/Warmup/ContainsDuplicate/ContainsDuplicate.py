#BruteForce
class Solution:
  def contains_duplicate(self, nums) -> bool:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]: # if any two elements are the same, return true
          return True
    return False # if no duplicates are found, return false

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.contains_duplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.contains_duplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.contains_duplicate(nums3)) # Expected output: False

  nums4 = [1, 1, 1, 1]
  print(sol.contains_duplicate(nums4)) # Expected output: True



#Sets
class Solution:
  def contains_duplicate(self, nums):
    unique_set = set() # Use set to store unique elements
    
    for x in nums:
      if x in unique_set: # If the set already contains the current element, return True
        return True
      unique_set.add(x) # Add the current element to the set

    return False # Return False if no duplicates found

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 4]
  print(sol.contains_duplicate(nums1)) # Expected output: False

  nums2 = [1, 2, 3, 1]
  print(sol.contains_duplicate(nums2)) # Expected output: True

  nums3 = []
  print(sol.contains_duplicate(nums3)) # Expected output: False

  nums4 = [1, 1, 1, 1]
  print(sol.contains_duplicate(nums4)) # Expected output: True
