//Brute Force
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  bool containsDuplicate(vector<int>& nums) {
    for (int i = 0; i < nums.size(); i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] == nums[j]) {
          return true; // if any two elements are the same, return true
        }
      }
    }
    return false; // if no duplicates are found, return false
  }
};

int main()
{
  Solution solution;
  vector<int> nums1 = {1, 2, 3, 4};
  cout << (solution.containsDuplicate(nums1) ? "true" : "false") << endl;

  vector<int> nums2 = {1, 2, 3, 1};
  cout << (solution.containsDuplicate(nums2) ? "true" : "false") << endl;

  vector<int> nums3 = {};
  cout << (solution.containsDuplicate(nums3) ? "true" : "false") << endl;

  vector<int> nums4 = {1, 1, 1, 1};
  cout << (solution.containsDuplicate(nums4) ? "true" : "false") << endl;
  return 0;
}

//Set
#include <unordered_set>
#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
  bool containsDuplicate(vector<int> &nums)
  {
    unordered_set<int> set;
    for (int x : nums)
    {
      if (set.count(x))
      {
        return true;
      }
      set.insert(x);
    }
    return false;
  }
};

int main()
{
  Solution solution;
  vector<int> nums1 = {1, 2, 3, 4};
  cout << (solution.containsDuplicate(nums1) ? "true" : "false") << endl;

  vector<int> nums2 = {1, 2, 3, 1};
  cout << (solution.containsDuplicate(nums2) ? "true" : "false") << endl;

  vector<int> nums3 = {};
  cout << (solution.containsDuplicate(nums3) ? "true" : "false") << endl;

  vector<int> nums4 = {1, 1, 1, 1};
  cout << (solution.containsDuplicate(nums4) ? "true" : "false") << endl;
  return 0;
}
