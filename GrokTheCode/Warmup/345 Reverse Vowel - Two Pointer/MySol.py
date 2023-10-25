class Solution:
    def reverseVowels(self, s: str) -> str:
        wordList = list(s)
        vowels = ['a', 'e', 'i', 'u', 'o', 'A', 'E', 'I', 'O', 'U']
        indexList = []
        vowelsFound = []
        curIndex = 0
        for char in s:
            if char in vowels:
                indexList.append(curIndex)
                vowelsFound.append(char)
            curIndex += 1
        iterList = len(indexList) - 1
        for vowel in vowelsFound:
            wordList[indexList[iterList]] = vowel
            iterList -= 1
        return "".join(wordList)