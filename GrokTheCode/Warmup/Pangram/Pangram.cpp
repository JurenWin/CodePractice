#include<iostream>
#include<unordered_set>
#include<ctype.h>

using namespace std;

class Solution {
  public:
    // Function to check if given sentence is pangram
    bool checkIfPangram(string sentence) {
        // Create a set to store unique characters
        unordered_set<char> seen;
        
        // Convert sentence to lowercase and iterate over each character
        for (char currChar : sentence) {
            if(isalpha(currChar)){
              seen.insert(tolower(currChar)); // Add the character to set
            }
        }
        
        // Return true if set size is 26 (total number of alphabets)
        return seen.size() == 26;
    }
};

int main() {
    Solution sol;

    // Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
    // Expected output: true
    cout << sol.checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog") << endl;

    // Test case 2: "This is not a pangram"
    // Expected output: false
    cout << sol.checkIfPangram("This is not a pangram") << endl;

    // Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
    // Expected output: true
    cout << sol.checkIfPangram("abcdef ghijkl mnopqr stuvwxyz") << endl;

    // Test case 4: ""
    // Expected output: false
    cout << sol.checkIfPangram("") << endl;

    // Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    // Expected output: true
    cout << sol.checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") << endl;

    return 0;
}
