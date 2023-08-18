class Solution:
    def remove_spaces(self, s: str) -> list[str]:
        words = s.split(' ')
        new_words = []
        for word in words:
            if word != '':
                new_words.append(word)
        return new_words

    def lengthOfLastWord(self, s: str) -> int:
        return len(self.remove_spaces(s)[-1])
