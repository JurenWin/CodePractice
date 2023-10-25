//Brute Force
class Solution {
  public boolean containsDuplicate(int[] nums) {
      for (int i = 0; i < nums.length; i++) {
          for (int j = i + 1; j < nums.length; j++) {
              if (nums[i] == nums[j]) { // if any two elements are the same, return true
                  return true;
              }
          }
      }
      return false; // if no duplicates are found, return false
  }

  public static void main(String[] args) {
    Solution solution = new Solution();

    int[] nums1 = {1, 2, 3, 4};
    System.out.println(solution.containsDuplicate(nums1)); // Expected output: false

    int[] nums2 = {1, 2, 3, 1};
    System.out.println(solution.containsDuplicate(nums2)); // Expected output: true

    int[] nums3 = {};
    System.out.println(solution.containsDuplicate(nums3)); // Expected output: false

    int[] nums4 = {1, 1, 1, 1};
    System.out.println(solution.containsDuplicate(nums4)); // Expected output: true
  }
}


//Sets
import java.util.HashSet;
import java.util.Set;

public class Solution {

  public boolean containsDuplicate(int[] nums) {
    Set<Integer> set = new HashSet<>(); // Use HashSet to store unique elements
    for (int x : nums) {
      if (!set.add(x)) // If the set already contains the current element, return true
        return true;
    }
    return false; // Return false if no duplicates found
  }

  public static void main(String[] args) {
    Solution solution = new Solution();

    int[] nums1 = {1, 2, 3, 4};
    System.out.println(solution.containsDuplicate(nums1)); // Expected output: false

    int[] nums2 = {1, 2, 3, 1};
    System.out.println(solution.containsDuplicate(nums2)); // Expected output: true

    int[] nums3 = {};
    System.out.println(solution.containsDuplicate(nums3)); // Expected output: false

    int[] nums4 = {1, 1, 1, 1};
    System.out.println(solution.containsDuplicate(nums4)); // Expected output: true
  }
}
