class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        const int maxNum = 100; // Given constraint: 1 <= nums[i] <= 100
        vector<int> count(maxNum + 1, 0); // Initialize an array to store counts
        
        int goodPairs = 0; // Initialize the count of good pairs
        
        // Iterate through the input array and calculate good pairs directly
        for (int num : nums) {
            goodPairs += count[num]; // Add the count of occurrences for the current number
            count[num]++; // Increment the count of the current number
        }
        
        return goodPairs; // Return the total count of good pairs
    }
};