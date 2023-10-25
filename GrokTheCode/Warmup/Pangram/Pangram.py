class Solution:
  def check_if_pangram(self, sentence):
    seen = set() # Create a set to store unique characters

    # Convert sentence to lowercase and iterate over each character
    for currChar in sentence.lower():
      if currChar.isalpha():
        seen.add(currChar) # Add the character to set

    # Return true if set size is 26 (total number of alphabets)
    return len(seen) == 26

# Test cases
sol = Solution()
# Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
# Expected output: True
print(sol.check_if_pangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

# Test case 2: "This is not a pangram"
# Expected output: False
print(sol.check_if_pangram("This is not a pangram"))

# Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
# Expected output: True
print(sol.check_if_pangram("abcdef ghijkl mnopqr stuvwxyz"))

# Test case 4: ""
# Expected output: False
print(sol.check_if_pangram(""))

# Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Expected output: True
print(sol.check_if_pangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
