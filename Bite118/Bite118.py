from collections import Counter

def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first occurrence.
       For example in the following list 'is' and 'it'
       occur more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    result = []
    words_counter = Counter(words)
    word_counts = words_counter.most_common()
    words_that_come_up_more_than_once = [i[0] for i in word_counts if i[1] >1]
    for w in words_that_come_up_more_than_once:
        result.append(words.index(w))
    return sorted(result)



input_list = ['this', 'is', 'a', 'new', 'bite', 'I', 'hope', 'this', 'bite', 'will', 'teach', 'you', 'something', 'new']

test = get_duplicate_indices(input_list)

print(test)