def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    result1 = ''
    for w in sorted(word1.lower()):
        if w != ' ':
            result1 += w.lower()

    result2 = ''
    for w in sorted(word2.lower()):
        if w != ' ':
            result2 += w.lower()

    return result1 == result2

a = is_anagram('William Shakespeare', 'I am a weakish speller')
print(a)