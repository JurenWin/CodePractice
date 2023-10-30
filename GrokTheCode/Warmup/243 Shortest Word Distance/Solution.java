
public class Shortest_Word_Distance {

    public static void main(String[] args) {
        Shortest_Word_Distance out = new Shortest_Word_Distance();
        Solution s = out.new Solution();

        System.out.println(s.shortestDistance(new String[]{"practice", "makes", "perfect", "coding", "makes"}, "makes", "coding"));
    }

    public class Solution {
        public int shortestDistance(String[] words, String word1, String word2) {
            int posA = -1;
            int posB = -1;
            int minDistance = Integer.MAX_VALUE;

            for (int i = 0; i < words.length; i++) {
                if (words[i].equals(word1)) {
                    posA = i;
                }

                if (words[i].equals(word2)) {
                    posB = i;
                }

                if (posA != -1 && posB != -1) { // will be run every time, after 1st pair is found
                    minDistance = Math.min(minDistance, Math.abs(posA - posB));
                }
            }

            return minDistance;
        }
    }
}

############

class Solution {
    public int shortestDistance(String[] wordsDict, String word1, String word2) {
        int ans = 0x3f3f3f3f;
        for (int k = 0, i = -1, j = -1; k < wordsDict.length; ++k) {
            if (wordsDict[k].equals(word1)) {
                i = k;
            }
            if (wordsDict[k].equals(word2)) {
                j = k;
            }
            if (i != -1 && j != -1) {
                ans = Math.min(ans, Math.abs(i - j));
            }
        }
        return ans;
    }
}