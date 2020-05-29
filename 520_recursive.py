class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1 and word[0].islower():
            return word[0].islower()
        elif len(word) == 1 and word[0].isupper():
            return word[0].isupper()
        elif word[0].islower():
            return word[0].islower() == word[1:].islower()
        elif word[0].isupper() and word[1].isupper():
            return word[0].isupper() == word[1:].isupper()
        else:
            return word[0].isupper() == word[1:].islower()
